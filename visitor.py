from AlgoritmosParserVisitor import AlgoritmosParserVisitor

class PseudocodigoVisitor(AlgoritmosParserVisitor):
    def __init__(self):
        self.output = []
        self.indent_level = 0

    def indent(self):
        return "    " * self.indent_level

    def visitProgram(self, ctx):
        self.output.append("INICIO")
        self.indent_level += 1

        for instr in ctx.instrucciones():
            self.visit(instr)

        self.indent_level -= 1
        self.output.append("FIN")
        return "\n".join(self.output)

    def visitLeer(self, ctx):
        vars = ctx.lista_id().getText().replace(",", ", ")
        self.output.append(f"{self.indent()}LEER {vars}")
        return ""

    def visitImprimir(self, ctx):
        expr = ctx.expresion().getText()
        self.output.append(f"{self.indent()}IMPRIMIR {expr}")
        return ""

    def visitAsignacion(self, ctx):
        var = ctx.ID().getText()
        expr = ctx.expresion().getText()
        self.output.append(f"{self.indent()}{var} ← {expr}")
        return ""

    def visitCondicion(self, ctx):
        cond = ctx.expresion().getText()
        self.output.append(f"{self.indent()}SI {cond} ENTONCES")

        self.indent_level += 1
        bloque_si = ctx.bloque(0)
        if bloque_si:
            for instr in bloque_si.instrucciones():
                self.visit(instr)
        self.indent_level -= 1

        if ctx.SINO():
            self.output.append(f"{self.indent()}SINO")
            self.indent_level += 1
            bloque_sino = ctx.bloque(1)
            if bloque_sino:
                for instr in bloque_sino.instrucciones():
                    self.visit(instr)
            self.indent_level -= 1

        self.output.append(f"{self.indent()}FIN_SI")
        return ""

    def visitMientras(self, ctx):
        cond = ctx.expresion().getText()
        self.output.append(f"{self.indent()}MIENTRAS {cond} HACER")

        self.indent_level += 1
        bloque = ctx.bloque()
        for instr in bloque.instrucciones():
            self.visit(instr)
        self.indent_level -= 1

        self.output.append(f"{self.indent()}FIN_MIENTRAS")
        return ""
