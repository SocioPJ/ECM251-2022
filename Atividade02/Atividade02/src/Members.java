public abstract class Members implements PostarMensagem{
    private final String nome;
    private final String email;
    private final EnumFuncoes funcao;
   
    
    public Members(String nome, String email, EnumFuncoes funcao) {
        this.nome = nome;
        this.email = email;
        this.funcao = funcao;
    }
    
    public String getNome() {
        return nome;
    }
    public String getEmail() {
        return email;
    }
    public EnumFuncoes getFuncao() {
        return funcao;
    }

    public void mudarTurno(){

    }

    @Override
    public String toString() {
        return "Members [email=" + email + ", funcao=" + funcao + ", nome=" + nome + "]";
    }
   
}
