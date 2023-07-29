package Models;

public class Toy implements Comparable<Toy> {
    private int id;
    private String name;
    private int count;
    private double weight;

    public Toy(int id, String name, int count) {
        this.id = id;
        this.name = name;
        this.count = count;
    }

    public int getId() {
        return id;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int value) {
        count = value;
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(int sumCount) {
        double scale = Math.pow(10, 2);
        weight = Math.round(count * 1.0 / sumCount * 100 * scale) / scale;
    }

    public String toString() {
        return this.name + " (id = " + this.id + ")";
    }

    @Override
    public int compareTo(Toy o) {
        return this.getWeight() > o.getWeight() ? -1 : 1;
    }
}
