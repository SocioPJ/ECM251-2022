public class Bicicleta extends Locomoção {
    public Bicicleta(String id, String tipo, double custo_hora) {
        super(id, tipo, custo_hora);
    }

    @Override
    public String toString() {
        return "id"+id+"tipo"+tipo+"custo_hora"+custo_hora;
    }
}
