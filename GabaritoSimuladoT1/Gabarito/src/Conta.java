public class Conta {
    private int idConta;
    private double saldo;
    private static int totalContas = 0;
    public Conta() {
        this.saldo = 0;
        this.idConta = totalContas;
        totalContas++;
    }
    public boolean depositar(double valor) {
        this.saldo += valor;
        return true;
    }
    public boolean sacar(double valor) {
        if (valor <= this.saldo) {
            this.saldo -= valor;
            return true;
        }
        return false;
    }
    public boolean transferir(Conta destino, double valor) {
        if(!sacar(valor))
            return false;
        return destino.depositar(valor);
    }
}
