/*
 * Необходимо написать программу – розыгрыша игрушек в магазине детских товаров.
 */
import Models.Shop;
import Presenters.Presenter;
import Views.View;

public class Program {
    public static void main(String[] args) {
        Shop shop = new Shop();
        View view = new View();
        Presenter presenter = new Presenter(shop, view);
        presenter.Run();
    }
}
