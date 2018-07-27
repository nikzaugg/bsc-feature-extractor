# bsc-feature-extractor
Extracts features between two versions of a file inside Gerrit Code Review.

## Overview
1. [Features](#features)  
1.1 [Code-Metrics](#code-metrics)  
1.2 [Change-Metrics](#change-metrics)  
1.3 [ASAT-Metrics](#asat-metrics)  
1.4 [CK-Metrics](#ck-metrics)  
1.5 [Low-level Source Code Changes](#low-level-source-code-changes)  
1.6 [Commit Messages](#commit-messages)  


## Features 

Feature | How it works
---|---
**Code-Metrics** | Static Code Information (SLOC, BLOC etc.)
**Change-Metrics** | Information about change information (Authors, Lines changed, Code Churn etc.)
**ASAT-Metrics** | Static Analysis Warnings from PMD and Checkstyle
**CK-Metrics** | Object-Oriented Information (WMC, DIT, etc.)
**Low-level Source Code Changes** | Low level change-types extracted from ChangeDistiller
**Commit Messages (NLP)** | Term frequency metrics of the commit message (tf-idf)



### Code-Metrics
* Physical Lines of Code (SLOC-P)
* Blank Lines of Code (BLOC)
* Comment Lines of Code (CLOC)
* Logical Lines of Code (SLOC-L)
* Cyclomatic Complexity Number (CCN) - McGabe metric


### Change-Metrics
* Number of Revisions of a file (NRev)
* Number of times a file has been refactored (Nrefac)
* Number of times a file was involved in bug-fixing (Nbugfix)
* Number of distinct authors that checked a file into the repository (NAuth)
* Sum/Max/Average over all revisions of the lines of code added to a file (LOCAdd)
* Sum/Max/Average over all revisions of the lines of code deleted from a file (LOCDelete)
* Sum/Max/Average of (added lines of code – deleted lines of code) over all revisions (CodeChurn)
* Maximum/Average number of files committed together to the repository (ChangeSet)
* Age of a file in weeks (counting backwards from a specific release) (Age)
* Weighted Age (WAge)


### ASAT-Metrics 
* Checkstyle Warnings
    * Mapped 180 Warnings into 16 Categories
* PMD Warnings
    * Mapped 330 Warnings into 16 Categories


### CK-Metrics
* Weighted Methods per Class (WMC)
* Depth of Inheritance Tree (DIT)
* Number of Children (NOC)
* Coupling Between Objects (CBO)
* Response For Class (RFC)
* Lack of Cohesion in Methods (LCOM)
* Number of Public Methods (NOPM)
* Afferent Couplings (Ca)
* Number of Methods (NOM)
* Number of Static Methods (NOSM)
* Number of Fields (NOF)
* Number of Public Fields (NOPF)
* Number of Static Fields (NOSF)
* Number of Static Invocations (NOSI)


### Low-level Source Code Changes
* 48 low-level change types extracted by the ChangeDistiller Tool


### Commit Messages
* NLP insights (word tokenizing, tf-idf etc.)

## Contributors
**Author:** [Nik Zaugg](https://github.com/nikzaugg)