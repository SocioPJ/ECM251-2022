public class Spock extends Jogada {
    public Spock() {
        super(EnumJogadas.TESOURA,EnumJogadas.PEDRA);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.SPOCK;
    }
}
