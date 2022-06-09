public class HeavyLifters extends Members {
    
    

    public HeavyLifters(String nome, String email, EnumFuncoes funcao) {
        super(nome, email, funcao);
        //TODO Auto-generated constructor stub
    }

    @Override
    public void postarMensagem() {
        if (Sistema.getHorario().equals(EnumHorario.REGULAR) ){
            System.out.println("Podem contar conosco!");
        }
        else if (Sistema.getHorario().equals(EnumHorario.EXTRA)){
            System.out.println("N00b_qu3_n_Se_r3pita.bat");
        }
        
        
    }
    
}