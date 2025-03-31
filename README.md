<h1 style="text-align: center">Visualizing Sorting Algorithms</h1>
<h2 style="text-align: center">GUI Edition</h2>

---
<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
- [Roadmap](#roadmap)
- [Support](#support)
- [License](#license)

</details>

---

## About

This project is a visualization of sorting algorithms. It is a simple web application that allows users to visualize the sorting process of various sorting algorithms. The project was created to help students understand how sorting algorithms work.

It is also my and my friend's TUBITAK 4006 project.

### Built With
- [tkinter](https://docs.python.org/3/library/tkinter.html)

## Getting Started
### Prerequisites
This project requires the following Python libraries:
- tkinter

However you don't need to install any of them since the GUI version of the app already includes them.

## Algorithms
The following algorithms are implemented in the project:
### 1 - Bubble Sort
This is one of the easiest algorithms in the project. Imagine you're organizing a deck of cards, and you're starting at one end. You compare two adjacent cards, and if the first one is bigger than the second, you swap them. Then, you move one card forward and do the same thing, comparing and swapping if needed, until you reach the end of the deck.

Now, after one complete pass through the deck, the largest card will have "bubbled up" to the end. You repeat this process for the remaining cards, ignoring the last one (since it's already in place), and keep doing this until the whole deck is sorted.

So, in simple terms: Bubble sort is like repeatedly pushing the biggest card to the back of the deck by comparing adjacent cards and swapping them.

### 2 - Insertion Sort
Figuring this out was really fun. Imagine you’re organizing a deck of cards, and you’re starting with the second card. You take that card and compare it with the card before it. If it's smaller, you slide the card to the left until it's in the right spot, pushing the larger cards to the right as you go.

Then, you move to the next card, compare it to all the cards before it, and slide it into its proper position. You keep repeating this process for each card in the deck, one by one, until all the cards are in order.

### 3 - Selection Sort
This is bland to be honest. Imagine you’re organizing a deck of cards, and you start by looking at all the cards to find the smallest one. Once you find it, you swap it with the card at the front of the deck.

Then, you move to the second card and repeat the process: look at the remaining cards, find the smallest one, and swap it with the second card. You continue this until you've gone through the entire deck, always selecting the smallest unsorted card and placing it in its correct position.

### 4 - Quick Sort
Imagine you’re organizing a deck of cards, and you choose one card to be your "pivot" card. You then go through the rest of the deck, placing all the cards smaller than the pivot on one side and all the cards larger than the pivot on the other side. Now, the pivot is in its correct spot.

Next, you repeat this process for the two groups of cards on either side of the pivot. Each group is treated like a smaller deck of cards, and you keep dividing and sorting them until every card is in its proper place.

### 5 - Heap Sort
Imagine you’re organizing a deck of cards, and you build a special kind of tree called a "heap" where each parent card is bigger (in a max heap) or smaller (in a min heap) than its child cards. You start by arranging all the cards into this heap structure.

Once the heap is built, you swap the top card (the largest, in a max heap) with the last card in the deck. Now, the largest card is in its correct position at the end. You then "reheapify" the remaining cards, making sure the heap property is restored, and repeat the process: swapping the top card with the last unsorted card and reheapifying the rest.

### 6 - Bogo Sort
Imagine you’re organizing a deck of cards, but instead of using any strategy, you just throw all the cards in the air and let them land randomly. Then, you check if the cards are in the correct order. If they’re not, you throw them up in the air again and repeat the process.

You keep doing this—shuffling the cards and checking—until the cards just happen to fall into the correct order by chance.

## Roadmap
- [x] Add more algorithms
  - [X] Bogo sort
  - [ ] Merge sort
  - [ ] Odd Even sort
  - [ ] Pancake sort
  - [ ] Shaker sort
  - [ ] Shell sort
  - [ ] Other weird algorithms 
- [x] Graphical User Interface

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. And that is how I learned to code. However since this is a school project, I cannot accept any contributions. But you can fork the project and make your own version of it.
Thank you for considering contributing to the project!

## Support
You may reach out to the maintainer of the project at:
- [GitHub Issues](https://github.com/axolotlagatsuma/visualizing-sorting-algorithms/issues)
- [X (formerly known as Twitter)](https://x.com/axolotlagatsuma)
- [E-mail (as mentioned in the profile README)](mailto:agatsuma@axolotldev.xyz)
- Discord (as mentioned in the profile README)
- Carrier pigeon

## License

This project is licensed under the **MIT license**. Feel free to edit and distribute this template as you like.

See [LICENSE](LICENSE) for more information.


