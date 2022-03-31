public class App {
    public static void main(String[] args) throws Exception {
       // System.out.println("Valor do contador:" + Exemplo.getContador());
        //Exemplo e1 = new Exemplo("Goku", 8001);
        //Exemplo e2 = new Exemplo("Vegeta", 8000);
        //System.out.println(e1);
        //System.out.println(e2);
        //System.out.println("Valor do contador:" + Exemplo.getContador());
        ValidadorCPF.validar("11111111111");
        System.out.println(""+ ValidadorCPF.validar("11111111111"));
        System.out.println(""+ ValidadorCPF.validar("52998224725"));
        System.out.println(""+ ValidadorCPF.validar("52998224735"));
        System.out.println(""+ ValidadorCPF.validar("52998224726"));

    }
}
