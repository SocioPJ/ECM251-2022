public class PokemonAgua extends Pokemon {
    public PokemonAgua(int numero, String nome, Status status) {
        super(numero, nome, status);
    }

    @Override
    public boolean evoluir(Status status) {
        if ( status == null)
            return false;
        Status atual = super.getStatus();
        return false;
    }
    
}
