public class Usuario {
    private String nome;
    private String veiculo_atual;
    //Construtor
    public Usuario(String nome, String veiculo_atual) {
        this.nome = nome;
        this.veiculo_atual = veiculo_atual;
    }
   
    //Métodos:
    public String getNome() {
        return nome;
    }
    public String getVeiculo_atual() {
        return veiculo_atual;
    }

    public void testar(String id, double custo_hora) {
        if (veiculo_atual.equals("Moto")) {
            Moto moto = new Moto(id, "Moto", Moto.custo_hora);
            System.out.println(moto.toString());
        } else if (veiculo_atual.equals("Patinete")) {
            Patinete patinete = new Patinete(id, "Patinete", Patinete.custo_hora);
            System.out.println(patinete.toString());
        } else if (veiculo_atual.equals("Bicicleta")) {
            Bicicleta bicicleta = new Bicicleta(id, "Bicicleta", Bicicleta.custo_hora);
            System.out.println(bicicleta.toString());
        } else if (veiculo_atual.equals("Carro")) {
            Carro carro = new Carro(id, "Carro", Carro.custo_hora);
            System.out.println(carro.toString());
        }
    }


    public void alugar(){

    }
}
