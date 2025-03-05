\documentclass{article}
\usepackage{hyperref}
\usepackage{graphicx}

\title{Simple Bidding Project}
\author{Uday Madivada}
\date{\today}

\begin{document}

\maketitle

\section{Description}
The \textbf{Simple Bidding Project} is a Python-based command-line program that allows multiple users to place bids in a simulated auction. The program collects bids from different users and determines the highest bidder. The project includes an ASCII art logo to enhance the user experience.

\section{Features}
\begin{itemize}
    \item Accepts multiple bids from users.
    \item Stores all bidding information in a dictionary.
    \item Determines and announces the highest bidder.
    \item Clears the screen after each entry for privacy.
    \item Two methods are used to find the highest bidder:
    \begin{enumerate}
        \item Using Python's \texttt{max()} function.
        \item Using a custom function \texttt{find\_highest\_bidder()}.
    \end{enumerate}
\end{itemize}

\section{Files Included}
\begin{itemize}
    \item \textbf{main.py} - The main script handling user input, bidding logic, and winner determination.
    \item \textbf{art.py} - Contains the ASCII art logo displayed at the beginning of the program.
\end{itemize}

\section{How to Run}
\begin{enumerate}
    \item Ensure you have \textbf{Python 3.x} installed.
    \item Clone the repository using:
    \begin{verbatim}
    git clone https://github.com/UdayMadivada25/SimpleBidding.git
    cd SimpleBidding
    \end{verbatim}
    \item Run the program:
    \begin{verbatim}
    python main.py
    \end{verbatim}
\end{enumerate}

\section{Example Usage}
\begin{verbatim}
What's your name? : Alice
Enter bidding amount: $100
Are there any other bidders? Type 'yes' or 'no': yes

What's your name? : Bob
Enter bidding amount: $150
Are there any other bidders? Type 'yes' or 'no': no

The winner is Bob with a bid of $150
\end{verbatim}

\section{License}
This project is open-source and free to use.

\section{Author}
Developed by \textbf{Uday Madivada}.

\end{document}
