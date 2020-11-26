var a,b:longint;
    d:array [0..1000000] of longint;
    q:array [0..1000000] of longint;
    f:text;
procedure doc;
var f:text;
begin
     assign(f,'biendoiso.inp');
     reset(f);
     read(f,a,b);
     close(f);
end;
procedure xuli;
var
    //q:array [0..1000000] of longint;
    bd,kt,u,i,x:longint;
begin
     for i:=1 to 1000000 do d[i]:=-1;
     d[a]:=0;
     bd:=1;
     kt:=1;
     q[1]:=a;

     while bd<=kt do
     begin
     u:=q[bd];
     inc(bd);

     x:=u shr 1;
     if d[x]=-1 then
     begin
     d[x]:=d[u]+1;
     inc(kt);
     q[kt]:=x;
     if x=b then exit;
     end;

     x:=u shl 1;
     if d[x]=-1 then
     begin
     d[x]:=d[u]+1;
     inc(kt);
     q[kt]:=x;
     if x=b then exit;
     end;

     x:=u+1;
     if d[x]=-1 then
     begin
     d[x]:=d[u]+1;
     inc(kt);
     q[kt]:=x;
     if x=b then exit;
     end;

     x:=u-1;
     if (d[x]=-1) and (x>=0) then
     begin
     d[x]:=d[u]+1;
     inc(kt);
     q[kt]:=x;
     if x=b then exit;
     end;

     end;


end;

BEGIN
     assign(f,'biendoiso.out');
     rewrite(f);
     doc;
     xuli;
     write(f,d[b]);

     close(f);
END.