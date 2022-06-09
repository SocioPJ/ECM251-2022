public class BigBrothers extends Members {

    

    public BigBrothers(String nome, String email, EnumFuncoes funcao) {
        super(nome, email, funcao);
        //TODO Auto-generated constructor stub
    }

    @Override
    public void postarMensagem() {
        if (Sistema.getHorario().equals(EnumHorario.REGULAR)){
            System.out.println("Sempre ajudando as pessoas membros ou não S2!");
        }
        else if (Sistema.getHorario().equals(EnumHorario.EXTRA)){
            System.out.println("...");
        }
        
        
    }
    
    public void cadastrarMembros(){
        System.out.println("Membro cadastrado com sucesso!");
    }
}