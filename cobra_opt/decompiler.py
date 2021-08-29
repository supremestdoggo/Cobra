import dis
import bytecode


def code_to_bytecode(code):
    """Converts a code object to a list of bytecode.Bytcode object."""
    dis_code = dis.Bytecode(code)
    instructions = []
    for instruction in dis_code:
        instructions.append(bytecode.Instr(instruction.opname, instruction.argval if instruction.arg != None else bytecode.UNSET))
    return bytecode.Bytecode(instructions)