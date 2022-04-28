public class Carro extends Locomoção {
    public Carro(String id, String tipo, double custo_hora) {
        super(id, tipo, custo_hora);
    }

    @Override
    public String toString() {
        return "id"+id+"tipo"+tipo+"custo_hora"+custo_hora;
    }
    
}
