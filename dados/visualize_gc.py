import matplotlib.pyplot as plt

# Data from our previous analysis
organisms = ['E. coli', 'B. subtilis', 'S. aureus']
gc_values = [54.45, 57.53, 51.00]

# Create the bar chart
plt.figure(figsize=(8, 6))
plt.bar(organisms, gc_values, color=['skyblue', 'salmon', 'lightgreen'])

# Adding labels and title
plt.xlabel('Organisms')
plt.ylabel('GC Content (%)')
plt.title('Comparative GC Content Analysis')
plt.ylim(40, 65)  # Setting the y-axis range to highlight the differences

# Save the plot as an image
plt.savefig('gc_comparison.png')
print("Graph saved as 'gc_comparison.png' successfully!")