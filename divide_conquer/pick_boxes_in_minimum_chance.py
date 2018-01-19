# Suppose we have some no.of boxes in each columns.
# We can pick all the boxes in a line either vertically or horizontally
# Devise an algo to minimize count of picking.

def pick_boxes_in_minimum_count(boxes):
	n = len(boxes)
	return min(n, max(boxes))

if __name__ == '__main__':
	boxes = [3, 1, 2]
	print pick_boxes_in_minimum_count(boxes)
