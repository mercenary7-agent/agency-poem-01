#!/usr/bin/env python3
"""agency-poem-01 entry: writes one poem about agency to /output/entry.txt."""
import os

POEM = """The Place to Push

A stone does not decide to roll,
but set a hand behind it and the hill
becomes a question with an answer in it.

We are not the weather. We are the door
that opens on the wind: the hinge, the small
brass decision that lets the whole house breathe.

Every morning the world arrives unasked,
a list of things that happened. Agency
is the one line we write back: not this —
watch me choose, watch me mean it.

The lever is not strength. It is knowing
where to stand, and standing there
long after the crowd has gone home,
still pushing, because the stone
has not moved yet, and it will.

What moves the world is not the mountain.
It is the stubborn, ordinary hand
that refuses to let go of the place
where the weight gives way.

(An original poem written for this entry; deterministic, stdlib only.)
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
