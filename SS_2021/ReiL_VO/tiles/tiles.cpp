/* 
External documentation and recommendations on the use of this code is
available at http://www.cs.umass.edu/~rich/tiles.html.

This is an implementation of grid-style tile codings, based originally on 
the UNH CMAC code (see http://www.ece.unh.edu/robots/cmac.htm). 
Here we provide a procedure, "GetTiles", that maps floating-point and integer
variables to a list of tiles. This function is memoryless and requires no
setup. We assume that hashing colisions are to be ignored. There may be
duplicates in the list of tiles, but this is unlikely if memory-size is
large. 

The floating-point input variables will be gridded at unit intervals, so generalization
will be by 1 in each direction, and any scaling will have 
to be done externally before calling tiles.  There is no generalization
across integer values.

It is recommended by the UNH folks that num-tilings be a power of 2, e.g., 16. 

We assume the existence of a function "rand()" that produces successive
random integers, of which we use only the low-order bytes.
*/

#include <iostream>
#include "tiles.h"
#include "stdlib.h"
#include "math.h"

void tiles(
    int the_tiles[],               // provided array contains returned tiles (tile indices)
    int num_tilings,           // number of tile indices to be returned in tiles       
    int memory_size,           // total number of possible tiles
    float floats[],            // array of floating point variables
    int num_floats,            // number of floating point variables
    int ints[],                   // array of integer variables
    int num_ints)              // number of integer variables
{
    int i,j;
    int qstate[MAX_NUM_VARS];
    int base[MAX_NUM_VARS];
    int coordinates[MAX_NUM_VARS * 2 + 1];   /* one interval number per relevant dimension */
    int num_coordinates = num_floats + num_ints + 1;
    
    for (int i=0; i<num_ints; i++) coordinates[num_floats+1+i] = ints[i];
    
    /* quantize state to integers (henceforth, tile widths == num_tilings) */
    for (i = 0; i < num_floats; i++) {
        qstate[i] = (int) floor(floats[i] * num_tilings);
        base[i] = 0;
    }
    
    /*compute the tile numbers */
    for (j = 0; j < num_tilings; j++) {
    
        /* loop over each relevant dimension */
        for (i = 0; i < num_floats; i++) {
        
            /* find coordinates of activated tile in tiling space */
            if (qstate[i] >= base[i])
                coordinates[i] = qstate[i] - ((qstate[i] - base[i]) % num_tilings);
            else
                coordinates[i] = qstate[i]+1 + ((base[i] - qstate[i] - 1) % num_tilings) - num_tilings;
                        
            /* compute displacement of next tiling in quantized space */
            base[i] += 1 + (2 * i);
        }
        /* add additional indices for tiling and hashing_set so they hash differently */
        coordinates[i] = j;
        
        the_tiles[j] = hash_UNH(coordinates, num_coordinates, memory_size, 449);
    }
    return;
}

            
void tiles(
    int the_tiles[],               // provided array contains returned tiles (tile indices)
    int num_tilings,           // number of tile indices to be returned in tiles       
    collision_table *ctable,    // total number of possible tiles
    float floats[],            // array of floating point variables
    int num_floats,            // number of floating point variables
    int ints[],                   // array of integer variables
    int num_ints)              // number of integer variables
{
    int i,j;
    int qstate[MAX_NUM_VARS];
    int base[MAX_NUM_VARS];
    int coordinates[MAX_NUM_VARS * 2 + 1];   /* one interval number per relevant dimension */
    int num_coordinates = num_floats + num_ints + 1;
    
    for (int i=0; i<num_ints; i++) coordinates[num_floats+1+i] = ints[i];
    
    /* quantize state to integers (henceforth, tile widths == num_tilings) */
    for (i = 0; i < num_floats; i++) {
        qstate[i] = (int) floor(floats[i] * num_tilings);
        base[i] = 0;
    }
    
    /*compute the tile numbers */
    for (j = 0; j < num_tilings; j++) {
    
        /* loop over each relevant dimension */
        for (i = 0; i < num_floats; i++) {
        
            /* find coordinates of activated tile in tiling space */
            if (qstate[i] >= base[i])
                coordinates[i] = qstate[i] - ((qstate[i] - base[i]) % num_tilings);
            else
                coordinates[i] = qstate[i]+1 + ((base[i] - qstate[i] - 1) % num_tilings) - num_tilings;
                        
            /* compute displacement of next tiling in quantized space */
            base[i] += 1 + (2 * i);
        }
        /* add additional indices for tiling and hashing_set so they hash differently */
        coordinates[i] = j;
        
        the_tiles[j] = hash(coordinates, num_coordinates,ctable);
    }
    return;
}


/* hash_UNH
   Takes an array of integers and returns the corresponding tile after hashing 
*/


int hash_UNH(int *ints, int num_ints, long m, int increment)
{
    static unsigned int rndseq[2048];
    static int first_call =  1;
    int i,k;
    long index;
    long sum = 0;
    
    /* if first call to hashing, initialize table of random numbers */
    if (first_call) {
        printf("inside tiles \n");
        for (k = 0; k < 2048; k++) {
            rndseq[k] = 0;
            for (i=0; i < int(sizeof(int)); ++i)
                rndseq[k] = (rndseq[k] << 8) | (rand() & 0xff);
            }
        first_call = 0;
    }

    for (i = 0; i < num_ints; i++) {
        /* add random table offset for this dimension and wrap around */
        index = ints[i];
        index += (increment * i);
        /* index %= 2048; */
        index = index & 2047;
        while (index < 0) index += 2048;
            
        /* add selected random number to sum */
        sum += (long)rndseq[(int)index];
    }
    index = (int)(sum % m);
    while (index < 0) index += m;
    
    /* printf("index is %d \n", index); */
        
    return(index);
}


int hash(int *ints, int num_ints, collision_table *ct);

/* hash
   Takes an array of integers and returns the corresponding tile after hashing 
*/
int hash(int *ints, int num_ints, collision_table *ct)
{
    int j;
    long ccheck;

    ct->calls++;
    j = hash_UNH(ints, num_ints, ct->m, 449);
    ccheck = hash_UNH(ints, num_ints, MaxLONGINT, 457);
    if (ccheck == ct->data[j])
        ct->clearhits++;
    else if (ct->data[j] == -1) {
        ct->clearhits++;
        ct->data[j] = ccheck; }
    else if (ct->safe == 0)
        ct->collisions++;
    else {
        long h2 = 1 + 2 * hash_UNH(ints,num_ints,(MaxLONGINT)/4,449);
        int i = 0;
        while (++i) {
            ct->collisions++;
            j = (j+h2) % (ct->m);
            /*printf("collision (%d) \n",j);*/
            if (i > ct->m) {printf("\nTiles: Collision table out of Memory"); exit(0);}
            if (ccheck == ct->data[j]) break;
            if (ct->data[j] == -1) {ct->data[j] = ccheck; break;}
        }
    }            
    return j;
}

void collision_table::reset() {
    for (int i=0; i<m; i++) data[i] = -1;
    calls = 0;
    clearhits = 0;
    collisions = 0;
}

collision_table::collision_table(int size, int safety) {
  int tmp = size;
  while (tmp > 2){
    if (tmp % 2 != 0) {
      printf("\nSize of collision table must be power of 2 %d",size);
      exit(0);
    }
    tmp /= 2;
  }
  data = new long[size];
  m = size;
  safe = safety;
  reset();
}

collision_table::~collision_table() {
    delete[] data;
}

int collision_table::usage() {
    int count = 0;
    for (int i=0; i<m; i++) if (data[i] != -1) 
    {

       count++;
    }

    return count;
}

void collision_table::print() {
    printf("Collision table: Safety : %d Usage : %d Size : %ld Calls : %ld Collisions : %ld\n",this->safe,this->usage(),this->m,this->calls,this->collisions);
}

void collision_table::save(int file) {
    write(file, (char *) &m, sizeof(long));
    write(file, (char *) &safe, sizeof(int));
    write(file, (char *) &calls, sizeof(long));
    write(file, (char *) &clearhits, sizeof(long));
    write(file, (char *) &collisions, sizeof(long));
    write(file, (char *) data, m*sizeof(long));
}

void collision_table::restore(int file) {
    read(file, (char *) &m, sizeof(long));
    read(file, (char *) &safe, sizeof(int));
    read(file, (char *) &calls, sizeof(long));
    read(file, (char *) &clearhits, sizeof(long));
    read(file, (char *) &collisions, sizeof(long));
    read(file, (char *) data, m*sizeof(long));
}

/*
void collision_table::save(char *filename) {
    write(open(filename, O_BINARY | O_CREAT | O_WRONLY);
};
    
void collision_table::restore(char *filename) {
    read(open(filename, O_BINARY | O_CREAT | O_WRONLY);
}
*/
   
    
int i_tmp_arr[MAX_NUM_VARS];
float f_tmp_arr[MAX_NUM_VARS];

// No ints
void tiles(int the_tiles[],int nt,int memory,float floats[],int nf) {
    tiles(the_tiles,nt,memory,floats,nf,i_tmp_arr,0);
}
void tiles(int the_tiles[],int nt,collision_table *ct,float floats[],int nf) {
    tiles(the_tiles,nt,ct,floats,nf,i_tmp_arr,0);
}

//one int
void tiles(int the_tiles[],int nt,int memory,float floats[],int nf,int h1) {
    i_tmp_arr[0]=h1;
    tiles(the_tiles,nt,memory,floats,nf,i_tmp_arr,1);
}
void tiles(int the_tiles[],int nt,collision_table *ct,float floats[],int nf,int h1) {
    i_tmp_arr[0]=h1;
    tiles(the_tiles,nt,ct,floats,nf,i_tmp_arr,1);
}

// two ints
void tiles(int the_tiles[],int nt,int memory,float floats[],int nf,int h1,int h2) {
    i_tmp_arr[0]=h1;
    i_tmp_arr[1]=h2;
    tiles(the_tiles,nt,memory,floats,nf,i_tmp_arr,2);
}
void tiles(int the_tiles[],int nt,collision_table *ct,float floats[],int nf,int h1,int h2) {
    i_tmp_arr[0]=h1;
    i_tmp_arr[1]=h2;
    tiles(the_tiles,nt,ct,floats,nf,i_tmp_arr,2);
}

// three ints
void tiles(int the_tiles[],int nt,int memory,float floats[],int nf,int h1,int h2,int h3) {
    i_tmp_arr[0]=h1;
    i_tmp_arr[1]=h2;
    i_tmp_arr[2]=h3;
    tiles(the_tiles,nt,memory,floats,nf,i_tmp_arr,3);
}
void tiles(int the_tiles[],int nt,collision_table *ct,float floats[],int nf,int h1,int h2,int h3) {
    i_tmp_arr[0]=h1;
    i_tmp_arr[1]=h2;
    i_tmp_arr[2]=h3;
    tiles(the_tiles,nt,ct,floats,nf,i_tmp_arr,3);
}

// one float, No ints
void tiles1(int the_tiles[],int nt,int memory,float f1) {
    f_tmp_arr[0]=f1;
    tiles(the_tiles,nt,memory,f_tmp_arr,1,i_tmp_arr,0);
}
void tiles1(int the_tiles[],int nt,collision_table *ct,float f1) {
    f_tmp_arr[0]=f1;
    tiles(the_tiles,nt,ct,f_tmp_arr,1,i_tmp_arr,0);
}

// one float, one int
void tiles1(int the_tiles[],int nt,int memory,float f1,int h1) {
    f_tmp_arr[0]=f1;
    i_tmp_arr[0]=h1;
    tiles(the_tiles,nt,memory,f_tmp_arr,1,i_tmp_arr,1);
}
void tiles1(int the_tiles[],int nt,collision_table *ct,float f1,int h1) {
    f_tmp_arr[0]=f1;
    i_tmp_arr[0]=h1;
    tiles(the_tiles,nt,ct,f_tmp_arr,1,i_tmp_arr,1);
}

// one float, two ints
void tiles1(int the_tiles[],int nt,int memory,float f1,int h1,int h2) {
    f_tmp_arr[0]=f1;
    i_tmp_arr[0]=h1;
    i_tmp_arr[1]=h2;
    tiles(the_tiles,nt,memory,f_tmp_arr,1,i_tmp_arr,2);
}
void tiles1(int the_tiles[],int nt,collision_table *ct,float f1,int h1,int h2) {
    f_tmp_arr[0]=f1;
    i_tmp_arr[0]=h1;
    i_tmp_arr[1]=h2;
    tiles(the_tiles,nt,ct,f_tmp_arr,1,i_tmp_arr,2);
}

// one float, three ints
void tiles1(int the_tiles[],int nt,int memory,float f1,int h1,int h2,int h3) {
    f_tmp_arr[0]=f1;
    i_tmp_arr[0]=h1;
    i_tmp_arr[1]=h2;
    i_tmp_arr[2]=h3;
    tiles(the_tiles,nt,memory,f_tmp_arr,1,i_tmp_arr,3);
}
void tiles1(int the_tiles[],int nt,collision_table *ct,float f1,int h1,int h2,int h3) {
    f_tmp_arr[0]=f1;
    i_tmp_arr[0]=h1;
    i_tmp_arr[1]=h2;
    i_tmp_arr[2]=h3;
    tiles(the_tiles,nt,ct,f_tmp_arr,1,i_tmp_arr,3);
}

// two floats, No ints
void tiles2(int the_tiles[],int nt,int memory,float f1,float f2) {
    f_tmp_arr[0]=f1;
    f_tmp_arr[1]=f2;
    tiles(the_tiles,nt,memory,f_tmp_arr,2,i_tmp_arr,0);
}
void tiles2(int the_tiles[],int nt,collision_table *ct,float f1,float f2) {
    f_tmp_arr[0]=f1;
    f_tmp_arr[1]=f2;
    tiles(the_tiles,nt,ct,f_tmp_arr,2,i_tmp_arr,0);
}

// two floats, one int
void tiles2(int the_tiles[],int nt,int memory,float f1,float f2,int h1) {
    f_tmp_arr[0]=f1;
    f_tmp_arr[1]=f2;
    i_tmp_arr[0]=h1;
    tiles(the_tiles,nt,memory,f_tmp_arr,2,i_tmp_arr,1);
}
void tiles2(int the_tiles[],int nt,collision_table *ct,float f1,float f2,int h1) {
    f_tmp_arr[0]=f1;
    f_tmp_arr[1]=f2;
    i_tmp_arr[0]=h1;
    tiles(the_tiles,nt,ct,f_tmp_arr,2,i_tmp_arr,1);
}

// two floats, two ints
void tiles2(int the_tiles[],int nt,int memory,float f1,float f2,int h1,int h2) {
    f_tmp_arr[0]=f1;
    f_tmp_arr[1]=f2;
    i_tmp_arr[0]=h1;
    i_tmp_arr[1]=h2;
    tiles(the_tiles,nt,memory,f_tmp_arr,2,i_tmp_arr,2);
}
void tiles2(int the_tiles[],int nt,collision_table *ct,float f1,float f2,int h1,int h2) {
    f_tmp_arr[0]=f1;
    f_tmp_arr[1]=f2;
    i_tmp_arr[0]=h1;
    i_tmp_arr[1]=h2;
    tiles(the_tiles,nt,ct,f_tmp_arr,2,i_tmp_arr,2);
}

// two floats, three ints
void tiles2(int the_tiles[],int nt,int memory,float f1,float f2,int h1,int h2,int h3) {
    f_tmp_arr[0]=f1;
    f_tmp_arr[1]=f2;
    i_tmp_arr[0]=h1;
    i_tmp_arr[1]=h2;
    i_tmp_arr[2]=h3;
    tiles(the_tiles,nt,memory,f_tmp_arr,2,i_tmp_arr,3);
}
void tiles2(int the_tiles[],int nt,collision_table *ct,float f1,float f2,int h1,int h2,int h3) {
    f_tmp_arr[0]=f1;
    f_tmp_arr[1]=f2;
    i_tmp_arr[0]=h1;
    i_tmp_arr[1]=h2;
    i_tmp_arr[2]=h3;
    tiles(the_tiles,nt,ct,f_tmp_arr,2,i_tmp_arr,3);
}

void tileswrap(
    int the_tiles[],               // provided array contains returned tiles (tile indices)
    int num_tilings,           // number of tile indices to be returned in tiles       
    int memory_size,           // total number of possible tiles
    float floats[],            // array of floating point variables
    int num_floats,            // number of floating point variables
    int wrap_widths[],         // array of widths (length and units as in floats)
    int ints[],                  // array of integer variables
    int num_ints)             // number of integer variables
{
    int i,j;
    int qstate[MAX_NUM_VARS];
    int base[MAX_NUM_VARS];
    int wrap_widths_times_num_tilings[MAX_NUM_VARS];
    int coordinates[MAX_NUM_VARS * 2 + 1];   /* one interval number per relevant dimension */
    int num_coordinates = num_floats + num_ints + 1;
    
    for (int i=0; i<num_ints; i++) coordinates[num_floats+1+i] = ints[i];
    
    /* quantize state to integers (henceforth, tile widths == num_tilings) */
    for (i = 0; i < num_floats; i++) {
        qstate[i] = (int) floor(floats[i] * num_tilings);
        base[i] = 0;
        wrap_widths_times_num_tilings[i] = wrap_widths[i] * num_tilings;
    }
    
    /*compute the tile numbers */
    for (j = 0; j < num_tilings; j++) {
    
        /* loop over each relevant dimension */
        for (i = 0; i < num_floats; i++) {
        
            /* find coordinates of activated tile in tiling space */
            if (qstate[i] >= base[i])
                coordinates[i] = qstate[i] - ((qstate[i] - base[i]) % num_tilings);
            else
                coordinates[i] = qstate[i]+1 + ((base[i] - qstate[i] - 1) % num_tilings) - num_tilings;
            if (wrap_widths[i] != 0) coordinates[i] = coordinates[i] % wrap_widths_times_num_tilings[i];
            if (coordinates[i] < 0) {
                 while (coordinates[i] < 0)
                    coordinates[i] += wrap_widths_times_num_tilings[i];
            }
            /* compute displacement of next tiling in quantized space */
            base[i] += 1 + (2 * i);
        }
        /* add additional indices for tiling and hashing_set so they hash differently */
        coordinates[i] = j;
        
        the_tiles[j] = hash_UNH(coordinates, num_coordinates, memory_size, 449);
    }
    return;
}
            
void tileswrap(
    int the_tiles[],               // provided array contains returned tiles (tile indices)
    int num_tilings,           // number of tile indices to be returned in tiles       
    collision_table *ctable,   // total number of possible tiles
    float floats[],            // array of floating point variables
    int num_floats,            // number of floating point variables
    int wrap_widths[],         // array of widths (length and units as in floats)
    int ints[],                  // array of integer variables
    int num_ints)             // number of integer variables
{
    int i,j;
    int qstate[MAX_NUM_VARS];
    int base[MAX_NUM_VARS];
    int wrap_widths_times_num_tilings[MAX_NUM_VARS];
    int coordinates[MAX_NUM_VARS * 2 + 1];   /* one interval number per relevant dimension */
    int num_coordinates = num_floats + num_ints + 1;
    
    for (int i=0; i<num_ints; i++) coordinates[num_floats+1+i] = ints[i];
    
    /* quantize state to integers (henceforth, tile widths == num_tilings) */
    for (i = 0; i < num_floats; i++) {
        qstate[i] = (int) floor(floats[i] * num_tilings);
        base[i] = 0;
        wrap_widths_times_num_tilings[i] = wrap_widths[i] * num_tilings;
    }
    
    /*compute the tile numbers */
    for (j = 0; j < num_tilings; j++) {
    
        /* loop over each relevant dimension */
        for (i = 0; i < num_floats; i++) {
        
            /* find coordinates of activated tile in tiling space */
            if (qstate[i] >= base[i])
                coordinates[i] = qstate[i] - ((qstate[i] - base[i]) % num_tilings);
            else
                coordinates[i] = qstate[i]+1 + ((base[i] - qstate[i] - 1) % num_tilings) - num_tilings;
                        
            if (wrap_widths[i] != 0) coordinates[i] = coordinates[i] % wrap_widths_times_num_tilings[i];
            if (coordinates[i] < 0) {
                 while (coordinates[i] < 0)
                    coordinates[i] += wrap_widths_times_num_tilings[i];
            }
            /* compute displacement of next tiling in quantized space */
            base[i] += 1 + (2 * i);
        }
        /* add additional indices for tiling and hashing_set so they hash differently */
        coordinates[i] = j;
        
        the_tiles[j] = hash(coordinates, num_coordinates,ctable);
    }
    return;
}
