import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class FoodOrder extends JFrame implements ActionListener {
    JTable menuTable;
    JTable cartTable;
    DefaultTableModel menuModel;
    DefaultTableModel cartModel;
    ArrayList<MenuItem> menuItems = new ArrayList<>();
    ArrayList<MenuItem> cartItems = new ArrayList<>();
    
    JTextField username;
    JPasswordField password;

    public FoodOrder() {
        showSignUp();
    }

    void showSignUp() {
        JPanel sign = new JPanel(new GridLayout(3, 2));
        username = new JTextField();
        password = new JPasswordField();
        JButton signup = new JButton("Sign up");

        sign.add(new JLabel("Username: "));
        sign.add(username);
        sign.add(new JLabel("Password: "));
        sign.add(password);
        sign.add(new JLabel(""));
        sign.add(signup);

        setTitle("Sign up - Food Ordering System");
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        add(sign);

        signup.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {
        String name = username.getText();
        String pword = new String(password.getPassword());
        JOptionPane.showMessageDialog(null, "Sign up successful for user: " + name);
        getContentPane().removeAll();
        showMainInterface();
        revalidate();
        repaint();
    }

    private void showMainInterface() {
        setTitle("Online Food Ordering System");
        setSize(800, 600);
        setLayout(new BorderLayout());

        menuItems.add(new MenuItem("Pizza", 100));
        menuItems.add(new MenuItem("Pasta", 150));
        menuItems.add(new MenuItem("Salad", 50));

        JPanel menuPanel = new JPanel(new BorderLayout());
        menuModel = new DefaultTableModel(new String[]{"Item", "Price"}, 0);
        menuTable = new JTable(menuModel);
        loadMenuItems();
        menuPanel.add(new JScrollPane(menuTable), BorderLayout.CENTER);

        JButton addToCartButton = new JButton("Add To Cart");
        menuPanel.add(addToCartButton, BorderLayout.SOUTH);
        add(menuPanel, BorderLayout.WEST);

        JPanel cartPanel = new JPanel(new BorderLayout());
        cartModel = new DefaultTableModel(new String[]{"Item", "Price"}, 0);
        cartTable = new JTable(cartModel);
        cartPanel.add(new JScrollPane(cartTable), BorderLayout.CENTER);

        JButton checkoutButton = new JButton("Checkout");
        cartPanel.add(checkoutButton, BorderLayout.SOUTH);
        add(cartPanel, BorderLayout.EAST);

        addToCartButton.addActionListener(e -> addToCart());
        checkoutButton.addActionListener(e -> checkout());
    }

    private void loadMenuItems() {
        for (MenuItem item : menuItems) {
            menuModel.addRow(new Object[]{item.getName(), item.getPrice()});
        }
    }

    private void addToCart() {
        int selectedRow = menuTable.getSelectedRow();
        if (selectedRow != -1) {
            String itemName = (String) menuModel.getValueAt(selectedRow, 0);
            double itemPrice = (double) menuModel.getValueAt(selectedRow, 1);
            cartItems.add(new MenuItem(itemName, itemPrice));
            cartModel.addRow(new Object[]{itemName, itemPrice});
        } else {
            JOptionPane.showMessageDialog(this, "Please select an item to add to cart.");
        }
    }

    private void checkout() {
        if (cartItems.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Your cart is empty.");
        } else {
            double total = 0;
            for (MenuItem item : cartItems) {
                total += item.getPrice();
            }
            JOptionPane.showMessageDialog(this, "Order placed! Total amount: $" + total);
            cartItems.clear();
            cartModel.setRowCount(0);
        }
    }

    static class MenuItem {
        private String name;
        private double price;

        public MenuItem(String name, double price) {
            this.name = name;
            this.price = price;
        }

        public String getName() {
            return name;
        }

        public double getPrice() {
            return price;
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            FoodOrder gui = new FoodOrder();
            gui.setVisible(true);
        });
    }
}
