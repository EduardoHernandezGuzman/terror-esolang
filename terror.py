#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TERROR — Intérprete minimalista inspirado en bolsilibros (v0)

Tokens: SILVER KANE, RALPH BARBY, CRIPTA, TUMBA, FRANK CAUDWELL,
        SUSURRO, CLARK CARRADOS, AMANECER.

Todo texto que no sea un token válido se ignora (prosa pulp).
"""
from __future__ import annotations
import argparse
import re
import sys
from typing import Dict, Iterable, List

TOKENS = [
    "SILVER KANE",    # +
    "RALPH BARBY",    # -
    "CRIPTA",         # >
    "TUMBA",          # <
    "FRANK CAUDWELL", # .
    "SUSURRO",        # ,
    "CLARK CARRADOS", # [
    "AMANECER",       # ]
]

TOKEN_RE = re.compile(r"\b(" + "|".join(map(re.escape, TOKENS)) + r")\b")


class Program:
    def __init__(self, source: str):
        self.code: List[str] = TOKEN_RE.findall(source)
        self.brackets: Dict[int, int] = self._build_brackets(self.code)

    @staticmethod
    def _build_brackets(code: List[str]) -> Dict[int, int]:
        stack: List[int] = []
        mapping: Dict[int, int] = {}
        for i, tok in enumerate(code):
            if tok == "CLARK CARRADOS":
                stack.append(i)
            elif tok == "AMANECER":
                if not stack:
                    raise SyntaxError(f"AMANECER sin CLARK CARRADOS (instr {i})")
                j = stack.pop()
                mapping[i] = j
                mapping[j] = i
        if stack:
            raise SyntaxError(f"CLARK CARRADOS sin AMANECER (instr {stack[-1]})")
        return mapping

    def run(self, input_bytes: Iterable[int] = ()) -> str:
        tape: List[int] = [0]
        ptr = 0
        ip = 0
        n = len(self.code)
        out_chars: List[str] = []
        inp = iter(input_bytes)

        while ip < n:
            tok = self.code[ip]
            if tok == "SILVER KANE":
                tape[ptr] = (tape[ptr] + 1) & 0xFF
            elif tok == "RALPH BARBY":
                tape[ptr] = (tape[ptr] - 1) & 0xFF
            elif tok == "CRIPTA":
                ptr += 1
                if ptr == len(tape):
                    tape.append(0)
            elif tok == "TUMBA":
                if ptr == 0:
                    tape.insert(0, 0)
                else:
                    ptr -= 1
            elif tok == "FRANK CAUDWELL":
                out_chars.append(chr(tape[ptr]))
            elif tok == "SUSURRO":
                try:
                    tape[ptr] = next(inp)
                except StopIteration:
                    tape[ptr] = 0
            elif tok == "CLARK CARRADOS":
                if tape[ptr] == 0:
                    ip = self.brackets[ip]
            elif tok == "AMANECER":
                if tape[ptr] != 0:
                    ip = self.brackets[ip]
            ip += 1
        return "".join(out_chars)


def to_bytes_from_text(s: str) -> List[int]:
    return list(s.encode("latin-1", "ignore"))


def main(argv: List[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Intérprete del esolang TERROR")
    p.add_argument("file", help="Ruta del programa .bolsi")
    p.add_argument("--input", dest="input_text", default="", help="Cadena de entrada (opcional)")
    p.add_argument("--trace", action="store_true", help="Muestra traza de ejecución")
    args = p.parse_args(argv)

    with open(args.file, "r", encoding="utf-8") as f:
        src = f.read()

    prog = Program(src)

    if args.trace:
        tape: List[int] = [0]
        ptr = 0
        ip = 0
        n = len(prog.code)
        out_chars: List[str] = []
        inp = iter(to_bytes_from_text(args.input_text))
        step = 0
        while ip < n:
            tok = prog.code[ip]
            before = (ip, ptr, tape[:8])
            if tok == "SILVER KANE":
                tape[ptr] = (tape[ptr] + 1) & 0xFF
            elif tok == "RALPH BARBY":
                tape[ptr] = (tape[ptr] - 1) & 0xFF
            elif tok == "CRIPTA":
                ptr += 1
                if ptr == len(tape):
                    tape.append(0)
            elif tok == "TUMBA":
                if ptr == 0:
                    tape.insert(0, 0)
                else:
                    ptr -= 1
            elif tok == "FRANK CAUDWELL":
                out_chars.append(chr(tape[ptr]))
            elif tok == "SUSURRO":
                try:
                    tape[ptr] = next(inp)
                except StopIteration:
                    tape[ptr] = 0
            elif tok == "CLARK CARRADOS":
                if tape[ptr] == 0:
                    ip = prog.brackets[ip]
            elif tok == "AMANECER":
                if tape[ptr] != 0:
                    ip = prog.brackets[ip]
            after = (ip, ptr, tape[:8])
            print(
                f"{step:05d} TOK={tok:<15} IP={before[0]:<4}->{after[0]+1:<4} PTR={before[1]:<3}->{after[1]:<3} TAPE={after[2]}",
                file=sys.stderr,
            )
            ip += 1
            step += 1
        sys.stdout.write("".join(out_chars))
    else:
        sys.stdout.write(prog.run(to_bytes_from_text(args.input_text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())