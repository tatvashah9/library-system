import functools
from datetime import datetime

def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper

def add_border(char="-", length=50):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            border = char * length
            return f"{border}\n{content}\n{border}"
        return wrapper
    return decorator

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] -> {func.__name__}() started")
        result = func(*args, **kwargs)
        print(f"[LOG] <- {func.__name__}() finished")
        return result
    return wrapper


class ReportSection:
    def __init__(self, title, content):
        self.title, self.content = title, content

    def __str__(self):
        return f"{self.title}\n{self.content}"

    def __repr__(self):
        return f"ReportSection(title={self.title!r})"

    def __eq__(self, other):
        return (isinstance(other, ReportSection)
                and self.title == other.title
                and self.content == other.content)


class Report:
    _templates = {}

    def __init__(self, title, author="Unknown"):
        self.title, self.author = title, author
        self.sections = []
        self.created_on = datetime.now()

    @classmethod
    def register_template(cls, name, section_titles):
        cls._templates[name] = section_titles
        print(f"[TEMPLATE] '{name}' registered with sections: {section_titles}")

    @classmethod
    def from_template(cls, name, title, author="Unknown"):
        if name not in cls._templates:
            raise ValueError(f"Template '{name}' is not registered")
        report = cls(title, author)
        for sec in cls._templates[name]:
            report.add_section(sec, "<content pending>")
        return report

    @classmethod
    def available_templates(cls):
        return list(cls._templates.keys())

    def add_section(self, title, content):
        self.sections.append(ReportSection(title, content))
        return self

    def set_content(self, title, content):
        for sec in self.sections:
            if sec.title == title:
                sec.content = content
                return True
        return False

    @log_call
    @add_border("=", 50)
    def summary(self):
        return (f"Report: {self.title}\n"
                f"Author: {self.author}\n"
                f"Sections: {len(self.sections)}\n"
                f"Generated: {self.created_on:%Y-%m-%d %H:%M}")

    @bold
    def title_line(self):
        return self.title

    def __str__(self):
        lines = [
            f"REPORT: {self.title}",
            f"Author: {self.author}",
            "-" * 40
        ]
        for sec in self.sections:
            lines += [str(sec), ""]
        return "\n".join(lines)

    def __repr__(self):
        return (f"Report(title={self.title!r}, "
                f"author={self.author!r}, "
                f"sections={len(self.sections)})")

    def __len__(self):
        return len(self.sections)

    def __getitem__(self, index):
        return self.sections[index]

    def __iter__(self):
        return iter(self.sections)

    def __contains__(self, title):
        return any(sec.title == title for sec in self.sections)

    def __add__(self, other):
        if not isinstance(other, Report):
            return NotImplemented
        merged = Report(f"{self.title} & {other.title}", self.author)
        merged.sections = self.sections + other.sections
        return merged

    def __eq__(self, other):
        return (isinstance(other, Report)
                and self.title == other.title
                and self.sections == other.sections)

    def __call__(self, formatter=None):
        text = str(self)
        return formatter(text) if formatter else text


if __name__ == "__main__":

    Report.register_template(
        "project_report",
        ["Introduction", "Methodology", "Results", "Conclusion"]
    )

    Report.register_template(
        "attendance_report",
        ["Summary", "Defaulter List"]
    )

    print("\nAvailable templates:", Report.available_templates())

    r1 = Report.from_template(
        "project_report",
        "AI Lab Mini Project",
        "Rahul"
    )

    r1.set_content(
        "Introduction",
        "This project explores dynamic report generation."
    )
    r1.set_content(
        "Methodology",
        "Used decorators, classmethods and magic methods."
    )
    r1.set_content(
        "Results",
        "Report generated and formatted successfully."
    )
    r1.set_content(
        "Conclusion",
        "OOP features simplify dynamic formatting."
    )

    r2 = Report("Attendance Snapshot", "Rahul")
    r2.add_section(
        "Summary",
        "92% average attendance this month."
    )

    print("\n--- len(r1) ---")
    print(len(r1))

    print("\n--- r1[0] ---")
    print(r1[0])

    print("\n--- iterate over r1 ---")
    for section in r1:
        print(" •", section.title)

    print("\n--- 'Results' in r1 ---")
    print("Results" in r1)

    print("\n--- combine r1 + r2 ---")
    print(r1 + r2)

    print("\n--- decorated summary() [bordered + logged] ---")
    print(r1.summary())

    print("\n--- title_line() [bold] ---")
    print(r1.title_line())

    print("\n--- report as callable, formatted UPPERCASE on the fly ---")
    print(r1(formatter=str.upper))

    print("\n--- report as callable, default (no formatter) ---")
    print(r2())