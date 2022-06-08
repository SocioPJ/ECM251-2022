public abstract class Pokemon implements Evoluir {
    private final int numero;
    private final String nome;
    private Status status;

    public Pokemon(int numero, String nome, Status status) {
        this.numero = numero;
        this.nome = nome;
        this.status = status;
    }
    protected void setStatus(Status status) {
        this.status = status;
    }

    public int getNumero() {
        return numero;
    }
    public String getNome() {
        return nome;
    }

    @Override
    public String toString() {
        return "Pokemon [nome=" + nome + ", numero=" + numero + ", status=" + status + "]";
    }

    public Status getStatus() {
        return status;
    }

    @Override
    public Status somarStatus(Status status, Status status2) {
        Status retorno = new Status(status.getVida() + status2.getVida(),
         status.getAtaque() + status2.getAtaque(),
          status.getDefensa() + status2.getDefensa(),
           status.getVelocidade() + status2.getVelocidade());
        return retorno;
    }
    
}