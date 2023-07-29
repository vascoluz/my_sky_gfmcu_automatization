#include <msp430.h> 
#include <stdint.h>


uint16_t ADC_Result_R_T1;//Valor de RT1
uint16_t ADC_Result_R_T2;//Valor de RT2
uint16_t AVG_ADC;//valor average da resistencia
uint8_t a = 0;//so uma simples variavel de controlo em uint8_t para ocupar menos espaço
int16_t erro_de_tensao = 0; //erro presente em relação a media das tensões pretendidas mantem-se em Q11

uint16_t VALOR_PERFECT_TENSAO = 512; //  1023 = 3.3  entao 465 =1.65V // valor que esta em Q11 //tava a dar um erro estupido por isso nao alterar


















void SET_PWM(void){//registo stat dp PWM

    //Para o driver
    P2DIR |= BIT1;            //set P2.1 as output
    P2SEL0  |= BIT1;
    P2SEL1  &= ~BIT1;  //registo principal TB1CCR  timerB1     TB1CRR0 controlo do periodo do timer B1  ,  TB1CCR2 valor onde o PWM para, TB1CCTL2 = OUTMOD_7; modo do timer TB1.2
    TB1CCR0 = 32788;       //f=61Hz             //funciona tambem para o adc            // PWM Period -> around 61 Hz
    TB1CCR2 = 3279*3; //timer 2 começa com fator de ciclo = 10%
    TB1CTL = TBSSEL__SMCLK | MC__UP | TBCLR | CNTL__16 | ID_3; // SMCLK/8, up mode //Defenição dos clocks para o TImER TB1
    TB1CCTL2 = OUTMOD_7; //RESET/SET


    // Para o adc
    TB1CCTL1 = OUTMOD_3;               //reset/set
    TB1CCR1 = 16394; //clock do para o outro
}


void set_FLL(void){
    //set do FLL para acertar a frequencia do low oscillator
    __bis_SR_register(SCG0); // enable global interrupts
    // FLL =  Frequency Locked Loop serve para estabiliza o low power oscillator
    CSCTL3 |= SELREF__REFOCLK;                         // Set REFO as FLL reference source //usa o low power oscillator  32768-Hz muita variancia
    CSCTL0 = 0;                                        // clear DCO and MOD registers de forma ao DCo começar do 0
    CSCTL1 &= ~(DCORSEL_7);  //limpar o select bits de frequencia
    CSCTL1 |= DCORSEL_5;                               // Set DCO = 16MHz
    CSCTL2 = FLLD_0 + 487;                             // FLLD_0 = 0 mas 16*10^6/487 = aprox 32768
    __delay_cycles(3); // esperar uns cliclos
    __bic_SR_register(SCG0);                           // enable FLL

    while(CSCTL7 & (FLLUNLOCK0 | FLLUNLOCK1));         // FLL locked, a espera que eles se sincronizem para continuar, enquanto FLLUNLOCK0
                                                       // FLLUNLOCK1 == 1 , significa que o DCO esta out of range e nao ta funcionar
}








int main(void)
{
	WDTCTL = WDTPW | WDTHOLD;	// stop watchdog timer
	


    P1SEL0 |= BIT5;   // configuração dos P1.5 como input do adc input 1 A5
    P1SEL1 |= BIT5;

    P1SEL0 |= BIT1;   // configuração dos P1.1 como input do adc input 2 A1
    P1SEL1 |= BIT1;

    FRCTL0 = FRCTLPW | NWAITS_1; //controlo da memoria ferroeletrica
                                    //FRCTLPW password. Always reads as 96h
                                    //Wait state control. Specifies number of wait states (0 to 7) required for an FRAM
                                    //access (cache miss). 0 implies no wait states.

    set_FLL();
    PM5CTL0 &= ~LOCKLPM5;



    //set do ADC
    ADCCTL0 |= ADCMSC | ADCON;                              // ADCON, S&H=16 ADC clks // ADC ta ON //sh =16 nao sei?
    ADCCTL1 |= ADCSHP | ADCSHS_2 | ADCSSEL_2 | ADCCONSEQ_2;             // ADCCLK = MODOSC; sampling timer //sampling do clock // repete sequencialmente os channels

    ADCCTL2 |= ADCRES; //defenir para 10 bits


    ADCMCTL0 |= ADCINCH_5 | ADCSREF_0;                        // A5 ADC input select; Vref=VCC Referencia interna do MSP430 FR2133 nao pode ser mudada.


    ADCIE |= ADCIE0;                                          // possiblilita interrupt do adc


        //Referencia
     PMMCTL0_H = PMMPW_H;                                      // Unlock the PMM registers
     PMMCTL2 |= INTREFEN;                                      // Enable internal reference ativa a internal reference, como ela nao e modificada assume-se que ela e i gual a 1.5V
     __delay_cycles(400);                                      // Delay for reference settling



     SET_PWM();


     ADCCTL0 |= ADCENC;                            // Sampling and conversion start


     __bis_SR_register(LPM0_bits | GIE); //da set em LOW power mode 0 e ativa o GIE Global interrupt routine





     while(1){

         if(a==2){
             AVG_ADC = ((ADC_Result_R_T1+ADC_Result_R_T2)>>1); // Q11+Q11 /2 tentativa
             erro_de_tensao = AVG_ADC-VALOR_PERFECT_TENSAO;


             a=0;//volta-se a por o 0 Para a medida
             ADCIE |= ADCIE0; //da enable aos interrupts

             //adicionar um delay de ciclos para nao ser instantanio mas para adicionar
             ADCCTL0 |= ADCENC;//liga-se o ADc
         }
     }

	return 0;
}


// ADC interrupt service routine
#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
#pragma vector=ADC_VECTOR
__interrupt void ADC_ISR(void)
#elif defined(__GNUC__)
void __attribute__ ((interrupt(ADC_VECTOR))) ADC_ISR (void)
#else
#error Compiler not supported!
#endif
{
    switch(__even_in_range(ADCIV,ADCIV_ADCIFG))
    {
        case ADCIV_NONE:
            break;
        case ADCIV_ADCOVIFG:
            break;
        case ADCIV_ADCTOVIFG:
            break;
        case ADCIV_ADCHIIFG:
            break;
        case ADCIV_ADCLOIFG:
            break;
        case ADCIV_ADCINIFG:
            break;
        case ADCIV_ADCIFG:

            if (a == 0 && ADCMCTL0 == ADCINCH_5){
                ADC_Result_R_T1 = ADCMEM0;
                __bic_SR_register_on_exit(LPM0_bits);              // Clear CPUOFF bit from LPM0
                a = 1;
                ADCCTL0 &= ~ADCENC; //desliga o ADC
                ADCMCTL0 &= ~ADCINCH_5;//desliga-se a entrada A5
                ADCMCTL0 |= ADCINCH_1;//liga-se a entrada A1
                ADCCTL0 |= ADCENC;// volta-se a ligar o ADC
                }
            else if (a == 1 && ADCMCTL0 == ADCINCH_1){
                ADC_Result_R_T2 = ADCMEM0;
                __bic_SR_register_on_exit(LPM0_bits);              // Clear CPUOFF bit from LPM0
                a = 2;
                ADCCTL0 &= ~ADCENC;//desliga-se o ADC
                ADCMCTL0 &= ~ADCINCH_1;//desliga-se a entrada A1
                ADCMCTL0 |= ADCINCH_5;//liga-se a entrada A5
                ADCIE &= ~ADCIE0; //da disable aos interrupts
                ADCIFG &= ~ADCIFG0;//limpa a flag do ADC tava a ficar stuck
                }


            break;
        default:
            break;
    }
}



















