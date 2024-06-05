# Level13

We have a binary expecting a the user to have a `UID` equal to `4242`.
By analysing it through gdb, we notice that a function `ft_des` is call with `boe]!ai0FB@.:|L6l@A?>qJ}I`
and apply many transformation on it. We can change the value of the register `eax` just before the comparation
in order to run `ft_des`. And we get the token