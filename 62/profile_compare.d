#pragma D option quiet
self int indent;

python$target:::function-entry
/basename(copyinstr(arg0)) == "portscanner_threads.py"
 && copyinstr(arg1) == "main"/
{
    self->trace = 1;
    self->last = timestamp;
}

python$target:::function-entry
/self->trace/
{
    this->delta = (timestamp - self->last) / 1000;
    printf("%d\t%*s:", this->delta, 15, probename);
    printf("%*s", self->indent, "");
    printf("%s:%s:%d\n", basename(copyinstr(arg0)), copyinstr(arg1), arg2);
    self->indent++;
    self->last = timestamp;
}

python$target:::function-return
/self->trace/
{
    this->delta = (timestamp - self->last) / 1000;
    self->indent--;
    printf("%d\t%*s:", this->delta, 15, probename);
    printf("%*s", self->indent, "");
    printf("%s:%s:%d\n", basename(copyinstr(arg0)), copyinstr(arg1), arg2);
    self->last = timestamp;
}

python$target:::function-return
/basename(copyinstr(arg0)) == "portscanner_threads.py"
 && copyinstr(arg1) == "main"/
{
    self->trace = 0;
}
