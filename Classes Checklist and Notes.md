# Notes and Progress Tracking

## General

A screen is represented by a `DisplayTerminal` instance. `DisplayTerminal`s 
contain a layout or presenter panel. `DisplayTerminal`s are 
a special case of the `Box` layout. When a `render()` or `update()` is called 
on the `DisplayTerminal` it then calls `render(row_number)` on the child 
layout/presenter. `DisplayTerminal`s are also intended to be the storage 
location for metadata regarding presentation to that player that would apply
to all child panels.
 
`panel.Render(row_number)` returns a string as long as the width of the panel 
instance. This width is determined during update calls based on the parent 
panels configuration and this panel's mode. Layout panels achieve this by 
calling their child panels, with some awareness of what children are in 
what rows.

Presenter panels are intended to format data, or even to be methods on 
actual data objects that return appropriate strings.

`render(row_number)` is intended to be adjusted for the offset of the panel 
within its parent, so that for the first row of the object you will make 
`row_number == 0`.  

The current design for inducing all this code to run is a callback based 
event system with per-event type subscription brokers. The main gotcha of 
this design is that every class that participates in the system needs to 
unsubscribe from all events when it is ready to be destroyed, or the Python
garbage collector will never get it.

Also, to reiterate some design goals. Screens shouldn't need to be stored as
a bunch of objects in the database. It may be necessary or beneficial to 
have screen descriptions of some sort stored, but I want as much as possible
for screens to be constructed at runtime from other arrangements 
of code.


## Classes to Write

#### Presenters:

* [Basic] `TextBlob` with paragraphs
* [Basic] `SimpleList`
* Inventory (Put this code in the Container class?)
* 2d arrays? (tabular data?)

#### Layouts:

* `Column`: Vertically arranged, sub-sized by list of dims, support auto.
* `Row`: Horizontally arranged, sub-sized by list of dims, support auto.
* `Box`: Single item, no sub-size.
* [Basic] `ColumnSplit`: 'pages' contents across columns, sub-sized by column 
count, and maybe other stuff.
* [Nixed] `SimpleGrid`: evenly divides (based on what?)

#### Master:

* [Critical] `DisplayTerminal`: Instanced per player. Dimensions set based on 
"physical" screen size or terminal window size. Maybe will need user 
settings to cover that instead.


## Primary TODO

* Address communication from the game to the presenters.
* Address whole screen changes for things like main menu, general play, 
inventory screens.


## Other TODO

* [Maybe] Data validation.
* Implement generalized 'auto' feature
* More formatted text: indents, colors.


## Capabilities Wishlist

* Scrolling
* Modal Dialog popups: Arbitrarily positioned Master panels that display 
over top of whatever else is going on, then return control to 
`DisplayTerminal` when closed.

# Code Key

* [Maybe] I'm not sure I need to spend effort on these.
* [Basic] I've gotten a functional skeleton going, but needs more work.
* [Complete] At this stage this appears to be done.
* [Nixed] Abandoned idea, mostly kept to remind me not to reinvent it later.
* [Critical] Until this changes status the system doesn't make sense.
