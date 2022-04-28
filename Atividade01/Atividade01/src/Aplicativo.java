public class Aplicativo {
    public static void run(){
        Carro carro = new Carro(Carro.gerarID(), "Carro", 20.0);
        Bicicleta bicicleta = new Bicicleta(Bicicleta.gerarID(), "Bicicleta", 10.0);
        Patinete patinete = new Patinete(Patinete.gerarID(), "Patinete", 5.0);
        Moto moto = new Moto(Moto.gerarID(), "Moto", 500.0);
        Usuario usuario = new Usuario("João", "Carro");
        usuario.testar(carro.getId(), carro.getCusto_hora());
    }
}
