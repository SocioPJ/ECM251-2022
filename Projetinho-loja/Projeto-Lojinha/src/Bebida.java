public class Bebida extends Produto {
    private final int volume;
    private final EnumTipoBebida tipo;
    private final EnumTemperaturas temperatura;
    private final EnumAlergias alergia;
    public Bebida(double preco, int quantidade, String descricao, String nome, int volume, EnumTipoBebida tipo,
            EnumTemperaturas temperatura, EnumAlergias alergia) {
        super(preco, quantidade, descricao, nome);
        this.volume = volume;
        this.tipo = tipo;
        this.temperatura = temperatura;
        this.alergia = alergia;
    }
    public int getVolume() {
        return volume;
    }
    public EnumTipoBebida getTipo() {
        return tipo;
    }
    public EnumTemperaturas getTemperatura() {
        return temperatura;
    }
    public EnumAlergias getAlergia() {
        return alergia;
    }

}
