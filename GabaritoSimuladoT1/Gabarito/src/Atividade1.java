public class Atividade1 {
    public static void run(){
        Usuario usuario1 = new Usuario("Joao", "123454","naotenhoemail@gmail.com" );
        Usuario usuario2 = new Usuario("Lucas", "563134","bfdfvssgfsb@gmail.com" );
        Usuario usuario3 = new Usuario("Minato", "862135","akyhrrwrwrhwr@gmail.com" );

        usuario1.getConta().depositar(1000);
        usuario2.getConta().depositar(250);
        usuario3.getConta().depositar(3000);
    }
}
