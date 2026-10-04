"""A small OOP1 demonstration for managing fictional citizen complaints."""


class Complaint:
    """Represent one public-service complaint."""

    total_created = 0

    def __init__(self, complaint_id, category, area, description):
        self.complaint_id = complaint_id
        self.category = category
        self.area = area
        self.description = description
        self.status = "Pending"
        self.department = "Unassigned"
        Complaint.total_created += 1

    def display_info(self):
        """Print the details of this complaint."""
        print(f"Complaint ID: {self.complaint_id}")
        print(f"Category: {self.category}")
        print(f"Area: {self.area}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")
        print(f"Department: {self.department}")

    def update_status(self, new_status):
        """Set a complaint status when it is one of the allowed values."""
        if self.is_valid_status(new_status):
            self.status = new_status
            print(f"Complaint {self.complaint_id} status updated.")
            return True

        print("Invalid status. Use Pending, In Progress, or Resolved.")
        return False

    def assign_department(self, department_name):
        """Set the department responsible for this complaint."""
        self.department = department_name

    @classmethod
    def get_total_created(cls):
        """Return the number of Complaint objects created."""
        return cls.total_created

    @staticmethod
    def is_valid_status(status):
        """Return whether status is an allowed complaint status."""
        valid_statuses = ("Pending", "In Progress", "Resolved")
        return status in valid_statuses


class Department:
    """Represent a department that handles one complaint category."""

    def __init__(self, department_name, supported_category):
        self.department_name = department_name
        self.supported_category = supported_category

    def receive_complaint(self, complaint):
        """Assign a complaint if its category matches this department."""
        if complaint.category.casefold() == self.supported_category.casefold():
            complaint.assign_department(self.department_name)
            print(
                f"Complaint {complaint.complaint_id} assigned to "
                f"{self.department_name}."
            )
            return True

        print(
            f"{self.department_name} does not handle "
            f"{complaint.category} complaints."
        )
        return False


def add_complaint(records, complaint):
    """Add a complaint object to a dictionary using its ID as the key."""
    if complaint.complaint_id in records:
        print(f"Complaint ID {complaint.complaint_id} already exists.")
        return False

    records[complaint.complaint_id] = complaint
    print(f"Complaint {complaint.complaint_id} added successfully.")
    return True


def display_all_complaints(records):
    """Display every complaint stored in the dictionary."""
    if not records:
        print("There are no complaints to display.")
        return

    for complaint in records.values():
        print("\n--------------------")
        complaint.display_info()


def main():
    """Run the fictional demonstration."""
    complaints = {}

    complaint1 = Complaint(
        "C001",
        "Roads",
        "Central Freetown",
        "A section of the road needs repair.",
    )
    complaint2 = Complaint(
        "C002",
        "Waste Collection",
        "Lumley",
        "Rubbish has not been collected this week.",
    )

    roads_department = Department("Roads Department", "Roads")
    waste_department = Department("Waste Department", "Waste Collection")

    roads_department.receive_complaint(complaint1)
    waste_department.receive_complaint(complaint2)

    add_complaint(complaints, complaint1)
    add_complaint(complaints, complaint2)

    complaint1.update_status("In Progress")

    print("\nTotal complaint objects created:",
          Complaint.get_total_created())
    print("Is 'Resolved' a valid status?",
          Complaint.is_valid_status("Resolved"))

    print("\nALL COMPLAINTS")
    display_all_complaints(complaints)


if __name__ == "__main__":
    main()
