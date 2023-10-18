-- creates trigger to decrease quantity of item after new order

CREATE TRIGGER DECREASE_QUANTITY
	AFTER
	INSERT ON orders FOR EACH ROW
	UPDATE items
	SET
	    quantity = quantity - NEW.number
	WHERE name = NEW.item_name;