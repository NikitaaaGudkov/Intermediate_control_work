package Presenters;

import java.util.InputMismatchException;

import Models.Shop;
import Models.Toy;
import Views.View;

/*
 * Класс, связывающий работу Модели и Вида. В нём определён метод, запускающий приложение.
 */
public class Presenter {
    private Shop shop;
    private View view;

    public Presenter(Shop shop, View view) {
        this.shop = shop;
        this.view = view;
    }

    public void Run() {
        while(true) {
            view.OutputText("Выберите действие:\n" + 
                            "add - добавить игрушки;\n" + 
                            "raffle - устроить розыгрыш\n" + 
                            "exit - выход из приложения");
            String action = view.InputText();
            switch (action) {
                case "add": {
                    try {
                        view.OutputText("Введите id игрушки:");
                        int id = view.InputNum();
                        view.OutputText("Введите название игрушки:");
                        String name = view.InputText();
                        view.OutputText("Введите количество этих игрушек:");
                        int count = view.InputNum();
                        Toy toy = new Toy(id, name, count);
                        shop.AddToys(toy);
                        view.OutputText("Игрушка успешно добавлена в магазин");
                    }
                    catch(InputMismatchException ex) {
                        System.err.println(ex.getMessage());
                        view.OutputText("Проверьте ввод. Id и количество игрушек должны быть положительными целыми числами.");
                        view.getiScanner().nextLine();
                    }
                    break;
                }
                case "raffle": {
                    view.OutputText("Устраиваем розыгрыш!");
                    Toy prize = shop.GetPrize();
                    if(prize == null) {
                        view.OutputText("В магазине нет игрушек!");
                    }
                    else {
                        view.OutputText("Победитель получает: " + prize.toString());
                        shop.SaveToFile(prize);
                    }
                    break;
                }
                case "exit": {
                    view.CloseScanner();
                    return;
                }
                default: {
                    view.OutputText("Нераспознанная команда \"" + action + "\"! Повторите ввод");
                }
            }
        }
    }
}
