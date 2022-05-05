public class Jogada {
    private EnumJogadas venco;
    public Jogada(EnumJogadas venco) {
        this.venco = venco;
    }

    public boolean verificarVenceu(Jogada jogada){
        if(jogada.getTipo().equals(venco))
            return true;
        return false;
    }

    public EnumJogadas getTipo(){
        return EnumJogadas.PAPEL;
    }
}