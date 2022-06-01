public class TestDriveArrayObjetos {
    public static void main(String[] args) {
        Caneta[] canetas;
        // Cria as referências para as canetas
        // ATENÇÃO: NAO CRIA AS INSTANCIAS!
        canetas = new Caneta[3];
        // Crianção das instâncias
        canetas[0] = new Caneta("Azul", 0.5);
        canetas[1] = new Caneta("Verde", 1.0);
        canetas[2] = new Caneta("Vermelha", 2.0);

        for(int i=0; i<canetas.length; i++) {
            System.out.println("Cor da caneta: "+canetas[i].cor);
        }

    }
}
