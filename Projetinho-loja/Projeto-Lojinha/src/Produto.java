public abstract class Produto{
    private final double preco;
    private int quantidade;
    private final String descricao;
    private final String nome;
    public Produto(double preco, int quantidade, String descricao, String nome) {
        this.preco = preco;
        this.quantidade = quantidade;
        this.descricao = descricao;
        this.nome = nome;
    }
}