import pyinputplus as pyip, sys, time
from stopwatch import clear_screen

class Order:

    """
    Representing a sandwich order system, allowing users to customize their sandwich
    and calculating the total cost.
    """

    # Price data for sandwich components
    prices = {'bread': {'wheat': 1.5, 'white': 1.2, 'sourdough': 1.8},
    'protein': {'chicken': 2.5, 'turkey': 2.8, 'ham': 2.0, 'tofu': 2.2},
    'cheese': {'cheddar': 0.5, 'swiss': 0.6, 'mozzarella': 0.4},
    'mayo': 0.2, 'mustard': 0.2, 'lettuce': 0.3, 'tomato': 0.3}

    # Orderable item categories
    items = ['Bread', 'Protein', 'Cheese', 'Mayo', 'Mustard', 'Lettuce', 'Tomato']

    def __init__(self):

        """
        Initializing an order with default attributes for sandwich components,
        total cost, and a record of items in the order.
        """

        self.bread = None
        self.protein = None
        self.cheese = None
        self.mayo = None
        self.mustard = None
        self.lettuce = None
        self.tomato = None
        self.total_cost = 0
        self.quantity = 0
        self.order_items = {}
        self.count = 0
        self.process_count = 0
        self.methods = [self._bread, self._protein, self._cheese, self._mayo,
        self._mustard, self._lettuce, self._tomato, self._display_order,
        self._calculator, self._new_order]

    def quit(self):

        """
        Allows the user to cancel the order or return to the current process.
        Handles previously completed orders if the user chooses to cancel.
        """

        clear_screen()
        quiting = pyip.inputMenu(['Continue Ordering', 'Cancel anyways'], numbered = True,
        prompt = 'You are about to cancel the order\n')
        if quiting == 'Continue Ordering':
            self.methods[self.process_count]()
        else:
            clear_screen()
            if self.count == 0:
                print('Order Cancelled')
                sys.exit()
            elif self.count == 1:
                print(f'Your previous completed order is: ${self.total_cost:.2f}')
                previous_order = pyip.inputMenu(['Yes', 'No'], numbered = True,
                prompt = 'Do you want to take this?')
            else:
                print(f'The price of your previous completed orders is: \
                ${self.total_cost:.2f}')
                previous_order = pyip.inputMenu(['Yes', 'No'], numbered = True,
                prompt = 'Do you want to take these?')
            clear_screen()
            if previous_order == 'Yes':
                print(f'Total: ${self.total_cost:.2f}')
                print("Thank you for your order!")
                sys.exit()
            else:
                print('Order Cancelled')
                sys.exit()

    def _bread(self):

        """
        Processes the bread selection step. Adds the selected bread's cost to the total.
        """

        clear_screen()
        self.bread = pyip.inputMenu(['wheat', 'white', 'sourdough', 'quit'],
        numbered=True, prompt="Choose bread type:\n")
        time.sleep(1)
        if self.bread != 'quit':
            self.total_cost += Order.prices['bread'][self.bread]
            self.order_items['Bread'] = self.bread
        else:
            self.quit()

    def _protein(self):

        """
        processes the protein selection process, updating the total cost
        and recording the choice in the order details. Allows backtracking.
        """

        clear_screen()
        self.protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu', 'previous',
        'quit'], numbered=True, prompt="Choose protein type:\n")
        time.sleep(1)
        if self.protein not in ('previous', 'quit'):
            self.total_cost += Order.prices['protein'][self.protein]
            self.order_items['Protein'] = self.protein
        else:
            if self.protein == 'previous':
                self.total_cost -= Order.prices['bread'][self.bread]
                del self.order_items['Bread']
                self._bread()
                self._protein()
            else:
                self.quit()

    def _cheese(self):

        """
        processes the cheese selection process, updating the total cost
        and recording the choice in the order details. Allows backtracking.
        """

        clear_screen()
        want_cheese = pyip.inputMenu(['Yes', 'No', 'previous', 'quit'],
        numbered = True, prompt = "Do you want cheese?\n")
        time.sleep(1)
        if want_cheese == 'Yes':
            clear_screen()
            self.cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella', 'previous',
            'quit'], numbered=True, prompt="Choose cheese type:\n")
            time.sleep(1)
            if self.cheese not in ('previous', 'quit'):
                self.total_cost += Order.prices['cheese'][self.cheese]
                self.order_items['Cheese'] = self.cheese
            else:
                if self.cheese == 'previous':
                    self.total_cost -= Order.prices['protein'][self.protein]
                    del self.order_items['Protein']
                    self._protein()
                    self._cheese()
                else:
                    self.quit()
        elif want_cheese == 'previous':
            self.total_cost -= Order.prices['protein'][self.protein]
            del self.order_items['Protein']
            self._protein()
            self._cheese()
        elif want_cheese == 'quit':
            self.quit()

    # other methods (_cheese, _mayo, _mustard, _lettuce, _tomato) omitted for brevity.
    # They follow a similar pattern, handling individual customization steps
    # and supporting "previous" and "quit" options.

    def _mustard(self):
        clear_screen()
        add_this = pyip.inputMenu(['Yes', 'No', 'previous', 'quit'], numbered = True,
        prompt = "Do you want mustard?\n")
        time.sleep(1)
        if add_this == 'Yes':
            self.total_cost += Order.prices['mustard']
            self.order_items['Mustard'] = 'mustard'
        elif add_this == 'previous':
            if 'Mayo' in self.order_items:
                self.total_cost -= Order.prices['mayo']
                del self.order_items['Mayo']
            self._mayo()
            self._mustard()
        elif add_this == 'quit':
            self.quit()

    def _mayo(self):
        clear_screen()
        add_this = pyip.inputMenu(['Yes', 'No', 'previous', 'quit'], numbered = True,
        prompt = "Do you want mayo?\n")
        time.sleep(1)
        if add_this == 'Yes':
            self.total_cost += Order.prices['mayo']
            self.order_items['Mayo'] = 'mayo'
        elif add_this == 'previous':
            if 'Cheese' in self.order_items:
                self.total_cost -= Order.prices['cheese'][self.cheese]
                del self.order_items['Cheese']
            self._cheese()
            self._mayo()
        elif add_this == 'quit':
            self.quit()

    def _lettuce(self):
        clear_screen()
        add_this = pyip.inputMenu(['Yes', 'No', 'previous', 'quit'], numbered = True,
        prompt = "Do you want lettuce?\n")
        time.sleep(1)
        if add_this == 'Yes':
            self.total_cost += Order.prices['lettuce']
            self.order_items['Lettuce'] = 'lettuce'
        elif add_this == 'previous':
            if 'Mustard' in self.order_items:
                self.total_cost -= Order.prices['mustard']
                del self.order_items['Mustard']
            self._mustard()
            self._lettuce()
        elif add_this == 'quit':
            self.quit()

    def _tomato(self):
        clear_screen()
        add_this = pyip.inputMenu(['Yes', 'No', 'previous', 'quit'], numbered = True,
        prompt = "Do you want tomato?\n")
        time.sleep(1)
        if add_this == 'Yes':
            self.total_cost += Order.prices['tomato']
            self.order_items['Tomato'] = 'tomato'
        elif add_this == 'previous':
            if 'Lettuce' in self.order_items:
                self.total_cost -= Order.prices['lettuce']
                del self.order_items['Lettuce']
            self._lettuce()
            self._tomato()
        elif add_this == 'quit':
            self.quit()

    def _display_order(self):
        display = ''
        for i, item in enumerate(Order.items):
            if item in self.order_items:
                if i > 2:
                    display += (f'{item:<7}\t\t-\t{self.order_items[item].title():<9} - \
${Order.prices[self.order_items[item]]:>5.2f}\n')
                else:
                    display += (f'{item:<7}\t\t-\t{self.order_items[item].title():<9} - \
${Order.prices[item.lower()][self.order_items[item]]:>5.2f}\n')
        clear_screen()
        print(display)
        print(f'Total: ${self.total_cost}')
        want = pyip.inputMenu(["Yes", 'No', 'previous', 'quit'], numbered = True,
        prompt = 'Is this exactly what you want?\n')
        time.sleep(2)
        if want == 'Yes':
            pass
        elif want == 'previous':
            if 'Tomato' in self.order_items:
                self.total_cost -= Order.prices['tomato']
                del self.order_items['Tomato']
            self._tomato()
            self._display_order()
        elif want == 'No':
            clear_screen()
            reorder = pyip.inputMenu(['reorder', 'previous', 'quit'], numbered = True)
            time.sleep(1)
            if reorder == 'reorder':
                Order().take_order()
                sys.exit()
            elif reorder == 'previous':
                if 'Tomato' in self.order_items:
                    self.total_cost -= Order.prices['tomato']
                    del self.order_items['Tomato']
                self._tomato()
                self._display_order()
            elif reorder == 'quit':
                pass
        else:
            self.quit()

    def _calculator(self):
        clear_screen()
        self.quantity = pyip.inputInt("How many sandwiches would you like to order?\n ", min=1)
        self.total_cost *= self.quantity
        print(f'Total: ${self.total_cost:.2f}')
        time.sleep(1)

    def take_order(self):
        clear_screen()
        print("Welcome to the Sandwich Maker!")
        time.sleep(1.5)
        for i, method in enumerate(self.methods):
            method()
            self.process_count = i
        return self

    def _new_order(self):
        new_cost = 0
        clear_screen()
        new_order = pyip.inputMenu(['Yes', 'No'], numbered = True,
        prompt = 'Do you want to take new order\n')
        if new_order == 'Yes':
            self.count += 1
            new = Order().take_order()
            new_cost = new.total_cost
        else:
            pass
        clear_screen()
        self.total_cost += new_cost
        print(f'Total: ${self.total_cost:.2f}')
        print("Thank you for your order!")
        time.sleep(1)
# Entry point of the program
if __name__ == '__main__':
    Order().take_order()
