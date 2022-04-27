public class Usuario {
    private String nome;
    private String senha;
    private String email;
    private Conta conta;
    //Construtor:
    public Usuario(String nome, String senha, String email) {
        this.nome = nome;
        this.senha = senha;
        this.email = email;
        this.conta = new Conta();
    }
    //Getters: 
    public String getNome() {
        return nome;
    }
    public Conta getConta() {
        return conta;
    }
    @Override
    public String toString() {
        return "Usuario [conta=" + conta + ", email=" + email + ", nome=" + nome + ", senha=" + senha + "]";
    }
    
}
