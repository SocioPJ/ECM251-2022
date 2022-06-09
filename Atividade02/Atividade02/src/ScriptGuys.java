public class ScriptGuys extends Members {

    

    public ScriptGuys(String nome, String email, EnumFuncoes funcao) {
        super(nome, email, funcao);
        //TODO Auto-generated constructor stub
    }

    @Override
    public void postarMensagem() {
        if (Sistema.getHorario().equals(EnumHorario.REGULAR)){
            System.out.println("Prazer em ajudar novos amigos de código!");
        }
        else if (Sistema.getHorario().equals(EnumHorario.EXTRA)){
            System.out.println("QU3Ro_S3us_r3curs0s.py");
        }
        
        
    }
    
}
    