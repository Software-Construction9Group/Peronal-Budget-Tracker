## Flowchart

```mermaid
flowchart TD
    A[Start Program] --> B[Input Weekly Budget]
    B --> C[Validate Budget]
    C -->|Valid| D[Enter Transactions]
    C -->|Invalid| B

    D --> E[Input Description]
    E --> F[Input Amount]
    F --> G[Validate Amount]

    G -->|Valid| H[Add Transaction]
    G -->|Invalid| D

    H --> I[Update Total Spending]
    I --> J[Check Budget Exceeded?]

    J -->|Yes| K[Display Warning]
    J -->|No| L[Continue]

    L --> M{Done?}
    M -->|No| D
    M -->|Yes| N[Print Summary]
    N --> O[Print Category Summary]
    O --> P[End Program]
```
Markdown
## Pseudocode
START
Create CategoryBudgetTracker object
INPUT weekly budget
WHILE budget is negative 
      Display error
      INPUT budget again
END WHILE

REPEAT
INPUT transaction description
IF description = "done" AND transactions < 5 
    Display message : minimum 5 transactions 
required 
    CONTINUE 
END IF
IF description = "done"
   BRAEK
END IF 
INPUT transaction amount
IF amount is negative 
   Display error 
   CONTINUE
END IF
Add transaction
Update total spending 
Check if budget exceeded
UNTIL user finishes 

Print final summary 
Print category summary

END
