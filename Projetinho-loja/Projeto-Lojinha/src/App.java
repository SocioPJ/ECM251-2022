public class App {
    public static void main(String[] args) throws Exception {
        Produto manga = new Literatura(29.90, 10, "Manga", "Manga", "Editora", "Autor", 100, EnumGeneroLiteratura.ROMANCE);
        Produto coca = new Bebida(5.90, 8, "bom", "Coca-cola", 350, EnumTipoBebida.REFRIGERANTE, EnumTemperaturas.FRIO, EnumAlergias.GLUTEN);
        Produto tepokki = new Comida(9.90, 10, "Tepokki", "Tepokki", 10, EnumTipoComida.APIMENTADA, "Brasil", EnumAlergias.GLUTEN);

        System.out.println("Preços Regulares: ");
        System.out.println(manga.getNome() + ": R$" + manga.getPreco());
        System.out.println(coca.getNome() + ": R$" + coca.getPreco());
        System.out.println(tepokki.getNome() + ": R$" + tepokki.getPreco());
    }
}
