public class MobileMembers extends Members {

   

    public MobileMembers(String nome, String email, EnumFuncoes funcao) {
        super(nome, email, funcao);
        //TODO Auto-generated constructor stub
    }

    @Override
    public void postarMensagem() {
        if (Sistema.getHorario().equals(EnumHorario.REGULAR)){
            System.out.println("Happy Coding!");
        }
        else if (Sistema.getHorario().equals(EnumHorario.EXTRA)){
            System.out.println("Happy_C0d1ng. Maskers");
        }
        
        
    }
}