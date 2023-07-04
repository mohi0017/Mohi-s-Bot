:- discontiguous male/1.
:- discontiguous female/1.
:- discontiguous parent/2.
:- discontiguous friend/2.
:- discontiguous husband/2.
:- discontiguous wife/2.
:- discontiguous spouse/2.
:- discontiguous sister/2.
:- discontiguous married/2.
:- discontiguous brother/2.
:- discontiguous father/2.
:- discontiguous mother/2.
:- discontiguous child/2.
:- discontiguous grandparent/2.
:- discontiguous grandchild/2.
:- discontiguous sibling/2.
:- discontiguous son/2.
:- discontiguous daughter/2.
:- discontiguous grandfather/2.
:- discontiguous grandmother/2.
:- discontiguous grandson/2.
:- discontiguous granddaughter/2.
:- discontiguous uncle/2.
:- discontiguous aunt/2.
:- discontiguous nephew/2.
:- discontiguous niece/2.
:- discontiguous cousin/2.
:- discontiguous half_sibling/2.
:- discontiguous step_sibling/2.
:- discontiguous ancestor/2.
:- discontiguous descendant/2.
:- discontiguous sister_in_law/2.
:- discontiguous brother_in_law/2.
:- discontiguous father_in_law/2.
:- discontiguous mother_in_law/2.
:- discontiguous nephew_in_law/2.
:- discontiguous niece_in_law/2.
:- discontiguous cousin_in_law/2.
:- discontiguous related/2.
:- discontiguous has/2.
male(john).
male(jim).
male(tom).
male(sam).
male(ethan).
male(liam).
male(max).
male(oliver).
male(ahmad).
male(ali).
male(ahmed).
male(khadim).

female(mary).
female(ann).
female(lisa).
female(sara).
female(emma).
female(mia).
female(lucy).
female(sophia).
female(hello).
female(are).
female(rizvi).

parent(john, jim).
parent(john, ann).
parent(john, lisa).
parent(john, tom).
parent(jim, sam).
parent(jim, sara).
parent(jim, lisa).
parent(jim, tom).
parent(tom, emma).
parent(tom, max).
parent(ann, emma).
parent(ann, max).
parent(lisa, lucy).
parent(lisa, sophia).
parent(lisa, oliver).
parent(sara, lucy).
parent(sara, sophia).
parent(sara, oliver).

husband(X, Y) :- parent(X, Z), male(X), parent(Y, Z), female(Y).
wife(X, Y) :- parent(X, Z), female(X), parent(Y, Z), male(Y).
spouse(X, Y) :- parent(X, Z), female(X), parent(Y, Z), male(Y).
sister(X, Y) :- female(X), parent(Z, X), parent(Z, Y), X \= Y.
married(X, Y) :- spouse(X, Y), spouse(Y, X).
brother(X, Y) :- male(X), parent(Z, X), parent(Z, Y), X \= Y.
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
child(X, Y) :- parent(Y, X).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
grandchild(X, Y) :- grandparent(Y, X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
son(X, Y) :- male(X), parent(Y, X).
daughter(X, Y) :- female(X), parent(Y, X).
grandfather(X, Y) :- male(X), grandparent(X, Y).
grandmother(X, Y) :- female(X), grandparent(X, Y).
grandson(X, Y) :- male(X), grandchild(X, Y).
granddaughter(X, Y) :- female(X), grandchild(X, Y).
uncle(X, Y) :- male(X), sibling(X, Z), parent(Z, Y).
aunt(X, Y) :- female(X), sibling(X, Z), parent(Z, Y).
nephew(X, Y) :- male(X), sibling(Z, Y), parent(Z, X).
niece(X, Y) :- female(X), sibling(Z, Y), parent(Z, X).
cousin(X, Y) :- parent(Z, X), parent(W, Y), sibling(Z, W).
half_sibling(X, Y) :- parent(Z, X), parent(Z, Y), parent(W, X), parent(V, Y), W \= V.
step_sibling(X, Y) :- parent(Z, X), parent(W, Y), parent(V, X), parent(V, Y), Z \= W.
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
descendant(X, Y) :- parent(Y, X).
descendant(X, Y) :- parent(Z, X), descendant(Z, Y).
sister_in_law(X, Y) :- female(X), (sibling(X, Z), spouse(Y, Z); spouse(Y, Z), sibling(X, Z)).
brother_in_law(X, Y) :- male(X), (sibling(X, Z), spouse(Y, Z); spouse(Y, Z), sibling(X, Z)).
father_in_law(X, Y) :- male(X), (spouse(Z, Y), parent(X, Z); parent(X, Z), spouse(Z, Y)).
mother_in_law(X, Y) :- female(X), (spouse(Z, Y), parent(X, Z); parent(X, Z), spouse(Z, Y)).
nephew_in_law(X, Y) :- male(X), (spouse(Z, Y), sibling(X, Z); sibling(X, Z), spouse(W, Y), sibling(Z, W)).
niece_in_law(X, Y) :- female(X), (spouse(Z, Y), sibling(X, Z); sibling(X, Z), spouse(W, Y), sibling(Z, W)).
cousin_in_law(X, Y) :- (spouse(Z, Y), cousin(X, Z)); (spouse(Z, Y), cousin(Z, W), sibling(W, X)).
related(X, Y) :- ancestor(X, Y).
related(X, Y) :- ancestor(Y, X).
related(X, Y) :- descendant(X, Y).
related(X, Y) :- descendant(Y, X).
related(X, Y) :- sibling(X, Y).
related(X, Y) :- sibling(Y, X).
related(X, Y) :- cousin(X, Y).
related(X, Y) :- cousin(Y, X).
related(X, Y) :- uncle(X, Y).
related(X, Y) :- aunt(X, Y).
related(X, Y) :- nephew(X, Y).
related(X, Y) :- niece(X, Y).
related(X, Y) :- brother_in_law(X, Y).
related(X, Y) :- sister_in_law(X, Y).
related(X, Y) :- father_in_law(X, Y).
related(X, Y) :- mother_in_law(X, Y).
related(X, Y) :- nephew_in_law(X, Y).
related(X, Y) :- niece_in_law(X, Y).
related(X, Y) :- cousin_in_law(X, Y).
related(X, Y) :- spouse(X, Z), related(Z, Y).
male('Good').
male('Lahore').
