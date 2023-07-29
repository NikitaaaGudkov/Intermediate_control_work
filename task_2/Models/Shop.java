package Models;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Random;

/*
 * Класс магазина, который содержит коллекцию игрушек типа Toy. Элементы в этой коллекции отсортированы по весу. 
 */
public class Shop {
    private int sumCount;
    private Queue<Toy> listToys;

    public Shop() {
        listToys = new PriorityQueue<Toy>();
        sumCount = 0;
    }

    /*
     * Добавление игрушек в коллекцию магазина. Вводится допущение, что одинаковые игрушки имеют одинаковый id, который вводит пользователь.
     */
    public void AddToys(Toy toy) {
        Boolean checkId = true;
        for (Toy item : listToys) {
            if(item.getId() == toy.getId()) {
                checkId = false;
                item.setCount(item.getCount() + toy.getCount());
            }
        }
        if(checkId) {
            listToys.add(toy);
        }
        sumCount += toy.getCount();
        UpdateList();
    }

    private void UpdateList() {
        List<Toy> tempArray = new ArrayList<Toy>();
        for (Toy item : listToys) {
            tempArray.add(item);
        }
        listToys.clear();
        for (Toy item : tempArray) {
            item.setWeight(sumCount);
            listToys.add(item);
        }
    }

    public Toy GetPrize() {
        if (sumCount == 0) {
            return null;
        }
        List<Toy> prizes = new ArrayList<Toy>();
        Toy prize = listToys.poll();
        prizes.add(prize);
        while(listToys.size() > 0 && listToys.peek().getWeight() == prize.getWeight()) {
            prizes.add(listToys.poll());
        }
        var randomNumber = new Random().nextInt(prizes.size());
        Toy result =  prizes.get(randomNumber);
        result.setCount(result.getCount() - 1);
        sumCount -= 1;
        if (result.getCount() == 0) {
            prizes.remove(result);
        }
        for (Toy toy : prizes) {
            listToys.add(toy);
        }
        UpdateList();
        return result;
    }

    public void SaveToFile(Toy toy) {
        try(FileWriter writer = new FileWriter("task_2\\prizes.txt", true))
        {
            writer.write(toy.toString() + "\n");            
            writer.flush();
            System.out.println("Данные успешно записаны в файл");
        }
        catch(IOException ex){
            System.out.println(ex.getMessage());
        } 
    }
}
