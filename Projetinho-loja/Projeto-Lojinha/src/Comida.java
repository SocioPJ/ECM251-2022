public class Comida extends Produto {
    private final double peso;
    private final EnumTipoComida tipo;
    private final String origem;
    private final EnumAlergias alergia;
    public Comida(double preco, int quantidade, String descricao, String nome, double peso, EnumTipoComida tipo,
            String origem, EnumAlergias alergia) {
        super(preco, quantidade, descricao, nome);
        this.peso = peso;
        this.tipo = tipo;
        this.origem = origem;
        this.alergia = alergia;
    }
    public double getPeso() {
        return peso;
    }
    public EnumTipoComida getTipo() {
        return tipo;
    }
    public String getOrigem() {
        return origem;
    }
    public EnumAlergias getAlergia() {
        return alergia;
    }
    @Override
    public double gerarPrecoComDesconto() {
        return getPreco() * 0.95;
    }

}
