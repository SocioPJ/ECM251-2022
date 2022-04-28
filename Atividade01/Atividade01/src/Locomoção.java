import java.util.concurrent.ThreadLocalRandom;

public class Locomoção {
    //Atributos
    protected static String id;
    protected String tipo;
    protected double custo_hora;
    // Construtor
    public Locomoção(String id, String tipo, double custo_hora) {
        Locomoção.id = gerarID();
        this.tipo = tipo;
        this.custo_hora = custo_hora;
    }
    // Métodos
    public static String gerarID() {
        int idAleatorio = ThreadLocalRandom.current().nextInt(10000, 100000);
        return String.format("%i", idAleatorio);  
    }
    public static String getId() {
        return id;
    }
    public double getCusto_hora() {
        return custo_hora;
    }
    @Override
    public String toString() {
        return "Locomoção [custo_hora=" + custo_hora + ", id=" + id + ", tipo=" + tipo + "]";
    }
}
