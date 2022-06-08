public class Status {
    private int vida;
    private int ataque;
    private int defensa;
    private int velocidade;
    public Status(int vida, int ataque, int defensa, int velocidade) {
        this.vida = vida;
        this.ataque = ataque;
        this.defensa = defensa;
        this.velocidade = velocidade;
    }
    public int getVida() {
        return vida;
    }
    public int getAtaque() {
        return ataque;
    }
    public int getDefensa() {
        return defensa;
    }
    public int getVelocidade() {
        return velocidade;
    }
    @Override
    public String toString() {
        return "Status [ataque=" + ataque + ", defensa=" + defensa + ", velocidade=" + velocidade + ", vida=" + vida
                + "]";
    }

}
