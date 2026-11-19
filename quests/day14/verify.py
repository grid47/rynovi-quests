"""Day 14 · Trust but verify

A model read 10 invoices and gave back JSON (see OUTPUTS below). Some of it is great, some is broken,
and some looks fine but the maths doesn't add up. Your code decides what goes into the database
and what a person has to check.

No API key needed. Run `python quest.py 14` after each TODO.
"""
from pydantic import BaseModel, Field, ValidationError  # noqa: F401

from quests.day14.outputs import OUTPUTS  # noqa: F401  (the 10 raw model replies)


class Line(BaseModel):
    # TODO 14.1 · description: str, qty: int (at least 1), unit_price: float (not negative)
    description: str
    qty: int = Field(ge=1)           # at least 1
    unit_price: float = Field(ge=0)  # not negative
    # pass


class Invoice(BaseModel):
    # TODO 14.1 · vendor: str, invoice_no: str, lines: list[Line], total: float (not negative)
    vendor: str
    invoice_no: str
    lines: list[Line]
    total: float = Field(ge=0)
    pass


def parse(raw: str) -> Invoice | None:
    """TODO 14.2 · Turn one raw model reply into an Invoice.
    Return None when it isn't valid JSON or doesn't match the schema (hint: Invoice.model_validate_json)."""
    try:
        return Invoice.model_validate_json(raw)
    except ValidationError:
        return None
    # raise NotImplementedError


def problems(inv: Invoice) -> list[str]:
    """TODO 14.3 · Check the invoice in plain Python and list what's wrong:
      "no lines"        when lines is empty
      "total mismatch"  when the sum of qty × unit_price differs from total by more than 1 rupee
    An invoice with nothing wrong gives []."""
    if len(inv.lines) == 0 or not inv.lines:
        return ["no lines"] #ValidationError("no lines")
    found = []

    net = sum(line.qty * line.unit_price for line in inv.lines)
    if abs(net - inv.total) > 1:
        found.append("total mismatch")

    return found
    # raise NotImplementedError


def route(raws: list[str]) -> dict[str, list[str]]:
    """TODO 14.4 · Sort every raw reply into {"accepted": [...], "review": [...]}.
      accepted: invoice_no of every invoice that parses and has no problems
      review:   invoice_no of invoices that parse but have problems,
                and "reply {i}" (i = position in raws, from 0) for replies that don't parse at all
    Keep the order of raws."""
    
    ret = {"accepted": [], "review": []}

    for i, raw in enumerate(raws):
        inv = parse(raw)
        if inv is None:
            ret["review"].append(f"reply {i}")
        elif problems(inv):
            ret["review"].append(inv.invoice_no)
        else:
            ret["accepted"].append(inv.invoice_no)

    return ret


    # raise NotImplementedError
