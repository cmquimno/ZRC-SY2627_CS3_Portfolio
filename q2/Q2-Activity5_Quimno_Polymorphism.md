ACTIVITY 5

1. What do all the methods (move(), special_move(), use()) in the previous activities have in common?
Answer: They all share the exact same method names across entirely different, unrelated classes. This allows them to act as a shared interface, meaning a single function or a single loop can execute them uniformly without needing to know the specific class type beforehand.

2. How does this activity show polymorphism in a gaming context?
Answer: It shows how a game engine can manage characters and inventory items efficiently. Instead of using messy 'if-else' statements to check every individual item or class type, the game can simply trigger a single generic command like ".use()" or ".special_move()". Each specific object automatically handles its own unique behavior at runtime.

3. Can you think of other examples where the same action behaves differently depending on the character or item?
Answer: 
- An interact() method: A Warrior class might smash a locked door open, a Locksmith class might lockpick it cleanly, and a Mage class might open it using a magic spell.
- An attack() method: Triggering an attack would execute a close-range sword slash if the player has a Melee Weapon equipped, but it would calculate a long-range projectile arrow trajectory if a Bow is equipped.