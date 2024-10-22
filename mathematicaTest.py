# redundant
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr

session = WolframLanguageSession()

LENGTH = 5
a1, b1 = 3, -5
a2, b2 = -3, 3
print(session.evaluate(wlexpr(f'NSolveValues[Sqrt[({a1}-a3)^2 + ({b1}-b3)^2]=={LENGTH} && Abs[3-a3]/Abs[-5-b3]==Abs[{a1}-{a2}]/Abs[{b1}-{b2}],'+r'{a3,b3}]')))